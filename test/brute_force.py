class LogEntry:
    def __init__(self, timestamp, log_type, severity):
        self.timestamp = timestamp
        self.log_type = log_type
        self.severity = severity

class LogMonitor:
    def __init__(self):
        self.log_entries = []

    def add_log_entry(self, timestamp, log_type, severity):
        # Check if the insertion command is one that should not produce output
        # if log_type == "INTERNAL_SERVER_ERROR" and severity == 23.72:
        #     with open('output.txt', 'a') as f:
        #         f.write("No output\n")
        #     return
        
        self.log_entries.append(LogEntry(timestamp, log_type, severity))
        with open('output_test.txt', 'a') as f:
            f.write("No output\n")


    def compute_min_max_mean(self, log_type=None, before=None, after=None):
        filtered_logs = self.log_entries
        if log_type:
            filtered_logs = [log for log in filtered_logs if log.log_type == log_type]
        if before:
            filtered_logs = [log for log in filtered_logs if log.timestamp < before]
        if after:
            filtered_logs = [log for log in filtered_logs if log.timestamp > after]

        if not filtered_logs:
            with open('output_test.txt', 'a') as f:
                # 0 0 0 
                f.write("Min: 0.0, Max: 0.0, Mean: 0.0\n")
            return

        min_severity = min(log.severity for log in filtered_logs)
        max_severity = max(log.severity for log in filtered_logs)
        mean_severity = sum(log.severity for log in filtered_logs) / len(filtered_logs)

        with open('output_test.txt', 'a') as f:
            # .6f and no trailing zeros
            min_severity = ('{:.6f}'.format(min_severity)).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(min_severity) else '{:.6f}'.format(min_severity)
            max_severity = ('{:.6f}'.format(max_severity)).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(max_severity) else '{:.6f}'.format(max_severity)
            mean_severity = ('{:.6f}'.format(mean_severity)).rstrip('0').rstrip('.') if '.' in '{:.6f}'.format(mean_severity) else '{:.6f}'.format(mean_severity)
            f.write(f"Min: {min_severity}, Max: {max_severity}, Mean: {mean_severity}\n")


def input_handler():
    with open('output_test.txt', 'w') as f:
        f.write("")
    monitor = LogMonitor()
    with open("./test_cases.txt", "r") as f:
        for query in f:
            query = query.strip()
            print(query)
            if ';' in query:
                splitted_query = query.split(";")
                monitor.add_log_entry(int(splitted_query[0]), splitted_query[1], float(splitted_query[2]))
            else:
                splitted_query = query.split(" ")
                if len(splitted_query) == 1:
                    monitor.compute_min_max_mean(log_type=splitted_query[0])
                elif len(splitted_query) == 2:
                    if splitted_query[0] == "BEFORE":
                        monitor.compute_min_max_mean(before=int(splitted_query[1]))
                    else:
                        monitor.compute_min_max_mean(after=int(splitted_query[1]))
                elif len(splitted_query) == 3:
                    if splitted_query[0] == "BEFORE":
                        monitor.compute_min_max_mean(log_type=splitted_query[1], before=int(splitted_query[2]))
                    else:
                        monitor.compute_min_max_mean(log_type=splitted_query[1], after=int(splitted_query[2]))

input_handler()


    