class LRUCache:
    # Brute Force Approach
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.timestamp = {}
        self.clock = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.clock += 1
            self.timestamp[key] = self.clock
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.clock += 1
        if key not in self.cache and len(self.cache) >= self.capacity:
            lru_key = min(self.timestamp, key = self.timestamp.get)
            del self.cache[lru_key]
            del self.timestamp[lru_key]
        self.cache[key] = value
        self.timestamp[key] = self.clock
'''

    def __init__(self, capacity: int):
        
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        
'''