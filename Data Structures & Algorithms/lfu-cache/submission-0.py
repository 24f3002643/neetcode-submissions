class LFUCache:
    # Brute Force Approach
    # Using three dict/ one dict with list of length three as value
    # first element of list will be value
    # second element will be counter
    # third elemenet will be timestamp
    # space complexity will be O(1)
    # time complexity of get() is O(1)
    # time complexity of put() is O(n)

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.time = 0
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.time += 1
        self.cache[key][2] = self.time
        self.cache[key][1] += 1
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        self.time +=  1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.time
            return  
        if len(self.cache) == self.capacity :
            min_key = min(self.cache.items(), key = lambda x : (x[1][1], x[1][2]))[0]
            del self.cache[min_key]
        self.cache[key] = [value, 1, self.time]
        return
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)