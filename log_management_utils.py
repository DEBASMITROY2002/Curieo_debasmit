from monotionic_stack_utils import PrefixSuffix

# It is a wrapper class which contains the timestamps and the log levels
class TimestampLoglevel:
    def __init__(self):
        self.timestamps = [] # Contains timestamps
        self.prefix_suffix = PrefixSuffix() # Contains log levels in PrefixSuffix Class Object

    # Add log to the timestamps and log levels
    def add_log(self, timestamp, log_level):
        self.timestamps.append(timestamp)
        self.prefix_suffix.add_element(log_level)

    # Get the log level at index i
    def get(self, i):
        return self.timestamps[i], self.prefix_suffix.arr[i]
    








class LogManager:
    def __init__(self):
        # Map of error message to individual TimestampLoglevel object which falls under that error message type
        self.err_to_logindex = {}
        # Contains the timestamps and log levels of all the logs to store a global view of all logs
        self.timestamp_loglevel = TimestampLoglevel()

    # Add log to the data structure
    def add_log(self, timestamp, log_message, log_level):
        self.timestamp_loglevel.add_log(timestamp, log_level) # Add log to the global view 
        self.update_err_to_logindex(log_message, timestamp,log_level) # Add log to the error message map   

    # Update the error message to log index map
    def update_err_to_logindex(self, log_message, timestamp,log_level):
        if log_message in self.err_to_logindex:
            self.err_to_logindex[log_message]["TimestampLoglevel"].add_log(timestamp, log_level)
        else:
            self.err_to_logindex[log_message] = {
                "TimestampLoglevel": TimestampLoglevel()
            }
            self.err_to_logindex[log_message]["TimestampLoglevel"].add_log(timestamp, log_level)

    #  1 timestamp; log_type; severity : Submit a new log entry to the platform. The program should store the log entry in a data structure.
    def submit_log_entry(self, timestamp, log_type, severity):
        self.add_log(timestamp, log_type, severity)
        return "No output"

    
    #  2 log_type: Compute the min, max, and mean severity of the log entry associated with the specified log type.
    def compute_log_type(self, log_type):
        if log_type in self.err_to_logindex:
            prefix_suffix = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix
            all_min = prefix_suffix.get_prefix_min(len(prefix_suffix.arr)-1)
            all_max = prefix_suffix.get_prefix_max(len(prefix_suffix.arr)-1)
            all_mean = prefix_suffix.get_prefix_mean(len(prefix_suffix.arr)-1)
            return (all_min, all_max, all_mean)
        else:
            return "No output"


    # Binary search to find the index of the log entry with the given timestamp
    # If the timestamp is not found and Query is BEFORE then return the index of the log entry just before the timestamp
    # If the timestamp is not found and Query is AFTER then return the index of the log entry just after the timestamp
    # If there multiple log entries with the same timestamp, return the index of the first log entry with the given timestamp in case of BEFORE query
    # If there multiple log entries with the same timestamp, return the index of the last log entry with the given timestamp in case of AFTER query
    def binary_search(self, arr, timestamp, is_before):
        left, right = 0, len(arr) - 1
        found_match = False
        result = -1

        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == timestamp:
                result = mid
                found_match = True
                if is_before:
                    right = mid - 1
                else:
                    left = mid + 1

            elif arr[mid] < timestamp:
                if is_before and not found_match:
                    result = mid
                left = mid + 1
            else:
                if not is_before and not found_match:
                    result = mid
                right = mid - 1

        if not found_match:
            if is_before:
                return result + 1
            else:
                # if result != 0:
                return result - 1
            
        return result


    #  3 BEFORE timestamp : Compute the min, max, and mean severity of all log entries occurring before the specified timestamp.
    def compute_before_timestamp(self, timestamp):
        index = self.binary_search(self.timestamp_loglevel.timestamps, timestamp, is_before=True)
        if index >= 1:
            min_ans = self.timestamp_loglevel.prefix_suffix.get_prefix_min(index-1)
            max_ans = self.timestamp_loglevel.prefix_suffix.get_prefix_max(index-1)
            mean_ans = self.timestamp_loglevel.prefix_suffix.get_prefix_mean(index-1)
            return (min_ans, max_ans, mean_ans)
        else:
            return (0.0, 0.0, 0.0)
    
    #  3 AFTER timestamp: Compute the min, max, and mean severity of all log entries occurring after the specified timestamp.
    def compute_after_timestamp(self, timestamp):
        index = self.binary_search(self.timestamp_loglevel.timestamps, timestamp, is_before=False)
        if index < len(self.timestamp_loglevel.timestamps) - 1 and index != -2:
            min_ans = self.timestamp_loglevel.prefix_suffix.get_suffix_min(index+1)
            max_ans = self.timestamp_loglevel.prefix_suffix.get_suffix_max(index+1)
            mean_ans = self.timestamp_loglevel.prefix_suffix.get_suffix_mean(index+1)
            return (min_ans, max_ans, mean_ans) 
        else:
            return (0.0, 0.0, 0.0)





    #  4 BEFORE log_type timestamp : Compute the min, max, and mean severity of all log entries occurring before the specified timestamp and associated with the specified log type.
    def compute_before_log_type_timestamp(self, log_type, timestamp):
        if log_type in self.err_to_logindex:
            index = self.binary_search(self.err_to_logindex[log_type]["TimestampLoglevel"].timestamps, timestamp, is_before=True)
            if index >= 1:
                min_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_prefix_min(index-1)
                max_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_prefix_max(index-1)
                mean_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_prefix_mean(index-1)
                return (min_ans, max_ans, mean_ans)
            else:
                return (0.0, 0.0, 0.0)
        else:
            return "No output"

    #  5 AFTER log_type timestamp: Compute the min, max, and mean severity of all log entries occurring after the specified timestamp and associated with the specified log type.
    def compute_after_log_type_timestamp(self, log_type, timestamp):
        if log_type in self.err_to_logindex:
            index = self.binary_search(self.err_to_logindex[log_type]["TimestampLoglevel"].timestamps, timestamp, is_before=False)
            if index < len(self.err_to_logindex[log_type]["TimestampLoglevel"].timestamps) - 1 and index != -2:
                min_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_suffix_min(index+1)
                max_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_suffix_max(index+1)
                mean_ans = self.err_to_logindex[log_type]["TimestampLoglevel"].prefix_suffix.get_suffix_mean(index+1)
                return (min_ans, max_ans, mean_ans)
            else:
                return (0.0, 0.0, 0.0)
        else:
            return "No output"

    # Display all logs
    def display_logs(self):
        for log in zip(self.timestamp_loglevel.timestamps, self.timestamp_loglevel.prefix_suffix.arr):
            print(log)


    def query(self, query:str):
        try:
            # Using string splitting to get the query type and the parameters
            # If the query contains a ';' then it is of type 1
            # If the query contains a ' ' then it is of type 2,3,4,5
            # Otherwise, it is of No output type
            if ';' in query:
                splitted_query = query.split(";")
                ans = self.submit_log_entry(int(splitted_query[0]), splitted_query[1], float(splitted_query[2]))
            else:
                splitted_query = query.split(" ")
                if len(splitted_query) == 1:
                    ans = self.compute_log_type(splitted_query[0])
                elif len(splitted_query) == 2:
                    if splitted_query[0] == "BEFORE":
                        ans = self.compute_before_timestamp(int(splitted_query[1]))
                    elif splitted_query[0] == "AFTER":
                        ans=self.compute_after_timestamp(int(splitted_query[1]))
                elif len(splitted_query) == 3:
                    if splitted_query[0] == "BEFORE":
                        ans=self.compute_before_log_type_timestamp(splitted_query[1], int(splitted_query[2]))
                    elif splitted_query[0] == "AFTER":
                        ans=self.compute_after_log_type_timestamp(splitted_query[1], int(splitted_query[2]))
                else:
                    print("No output")
                    return
            
            if type(ans) == tuple:
                v1 = (('{:.6f}'.format(ans[0])).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(ans[0]) else '{:.6f}'.format(ans[0])) if ans[0] != 0.0 else '0.0'
                v2 = (('{:.6f}'.format(ans[1])).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(ans[1]) else '{:.6f}'.format(ans[1])) if ans[1] != 0.0 else '0.0'
                v3 = (('{:.6f}'.format(ans[2])).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(ans[2]) else '{:.6f}'.format(ans[2])) if ans[2] != 0.0 else '0.0'
                print(f"Min: {v1}, Max: {v2}, Mean: {v3}")
                return f"Min: {v1}, Max: {v2}, Mean: {v3}"
            else:
                print(ans)
                return ans
        except:
            print("No output")
            return "No output"