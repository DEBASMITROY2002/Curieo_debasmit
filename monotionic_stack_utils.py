class PrefixSuffix:
    def __init__(self):
        self.arr = [] # Contains severity values
        self.prefix_min = [] # Prefix Min from 0 to i
        self.prefix_max = [] # Prefix Max from 0 to i
        self.suffix_min = [] # Monotonic Stack Contains (value, index) 
        self.suffix_max = [] # Monotonic Stack Contains (value, index)
        self.prefix_sum = [] # Prefix Sum from 0 to i
        self.total_sum = 0 # Total Sum of all elements

    # Add element to the array and update the prefix and suffix arrays
    def add_element(self, element):
        self.arr.append(element)
        self.update_prefix_min_max_sum()
        self.update_suffix_min_max()

    # Update the prefix arrays
    def update_prefix_min_max_sum(self):
        if len(self.arr) == 1:
            self.prefix_min.append(self.arr[0])
            self.prefix_max.append(self.arr[0])
            self.prefix_sum.append(self.arr[0])
        else:
            self.prefix_min.append(min(self.prefix_min[-1], self.arr[-1]))
            self.prefix_max.append(max(self.prefix_max[-1], self.arr[-1]))
            self.prefix_sum.append(self.prefix_sum[-1] + self.arr[-1])
        self.total_sum += self.arr[-1]
    
    # Update the suffix arrays using Monotonic Stack Paradigm
    def update_suffix_min_max(self):
        if len(self.arr) == 1:
            self.suffix_min.append((self.arr[0], 0))
            self.suffix_max.append((self.arr[0], 0))
        else:
            # Ammortized O(1) time complexity
            while self.suffix_min and self.suffix_min[-1][0] > self.arr[-1]:
                self.suffix_min.pop()
            
            # Ammortized O(1) time complexity
            while self.suffix_max and self.suffix_max[-1][0] < self.arr[-1]:
                self.suffix_max.pop()
            self.suffix_min.append((self.arr[-1], len(self.arr)-1))
            self.suffix_max.append((self.arr[-1], len(self.arr)-1))

    # Get the prefix min value from 0 to index
    def get_prefix_min(self,index):
        return self.prefix_min[index]
    
    # Get the prefix max value from 0 to index
    def get_prefix_max(self,index):
        return self.prefix_max[index]
    
    # Get the prefix mean value from 0 to index
    def get_prefix_mean(self,index):
        return self.prefix_sum[index]/(index+1)
    
    # Get the suffix min value from index to n-1
    # Uses Binary Search to find the required index in O(logn) time complexity
    def get_suffix_min(self,index):
        # Binary search to find the required index
        low = 0
        high = len(self.suffix_min)-1
        while low < high:
            mid = low + (high-low)//2
            if self.suffix_min[mid][1] == index:
                return self.suffix_min[mid][0]
            elif self.suffix_min[mid][1] < index:
                low = mid+1
            else:
                high = mid
        return self.suffix_min[low][0]
    
    # Get the suffix max value from index to n-1
    # Uses Binary Search to find the required index in O(logn) time complexity
    def get_suffix_max(self,index):
        # Binary search to find the required index
        low = 0
        high = len(self.suffix_max)-1
        while low < high:
            mid = low + (high-low)//2
            if self.suffix_max[mid][1] == index:
                return self.suffix_max[mid][0]
            elif self.suffix_max[mid][1] < index:
                low = mid+1
            else:
                high = mid
        return self.suffix_max[low][0]

    # Get the suffix mean value from index to n-1 using the formula: (Total Sum - Prefix Sum + Current Element) / (n-index)
    def get_suffix_mean(self,index):
        return (self.total_sum - self.prefix_sum[index]+self.arr[index])/(len(self.arr)-index)
