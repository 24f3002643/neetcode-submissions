class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash_set = [Node() for i in range(10000)]

    def add(self, key: int) -> None:
        cur = self.hash_set[key % 10000]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = Node(key)
        

    def remove(self, key: int) -> None:
        cur = self.hash_set[key % 10000]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.hash_set[key % 10000]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)