class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, key):
        newNode = Node(key)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.tail
            temp.next = newNode
            newNode.prev = temp
            self.tail = newNode
    
    def appendAtEnd(self, pointer):
        if self.head.next is None:
            return
        if self.tail is pointer:
            return
        temp = pointer
        prev = temp.prev
        next = temp.next
        prev.next = next
        next.prev = prev
        temp.prev = self.tail
        temp.next = None
        self.tail.next = temp
        self.tail = temp

    def removeAtHead(self):
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        temp.next = None

class LRUCache:
    # Brute Force Approach
    '''
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
    # Optimized Approach
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mapping = {}
        self.doubleList = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.doubleList.appendAtEnd(self.mapping[key])
            return self.cache[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.doubleList.appendAtEnd(self.mapping[key])
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.pop(self.doubleList.head.value)
                self.mapping.pop(self.doubleList.head.value)
                self.doubleList.removeAtHead()
                self.cache[key] = value
                self.doubleList.append(key)
                self.mapping[key] = self.doubleList.tail
            else:
                self.doubleList.append(key)
                self.cache[key] = value
                self.mapping[key] = self.doubleList.tail
                
        
