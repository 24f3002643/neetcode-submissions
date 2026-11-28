class MyHashSet:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        for i in self.hash_set:
            if i == key:
                return
        self.hash_set.append(key)

    def remove(self, key: int) -> None:
        for i in self.hash_set:
            if i==key:
                self.hash_set.remove(key)


    def contains(self, key: int) -> bool:
        for i in self.hash_set:
            if i==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)