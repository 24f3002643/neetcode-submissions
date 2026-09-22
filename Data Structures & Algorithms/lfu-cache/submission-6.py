class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 0
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def __len__(self):
        count = 0
        node = self.head.next
        while node is not self.tail:
            count += 1
            node = node.next
        return count

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {} # to store the address of node
        self.freq_to_list = {} # to store the doubly linked list per frequency
        self.min_freq = 0 # to store the minimum frequency
        self.capacity = capacity
    def _remove(self, node):
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous
        return
    
    def _insert(self, freq, node):
        previous = self.freq_to_list[freq].tail.prev
        # self.freq_to_list[freq] gives the Doubly Linked List
        # then .tail on that list gives the last dummy node
        # then .prev gives the actual last node
        node.prev = previous
        node.next = self.freq_to_list[freq].tail
        previous.next = node
        tail = self.freq_to_list[freq].tail
        tail.prev = node
        return 

    
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        old_freq = node.freq
        new_freq = old_freq + 1
        self._remove(node)
        if len(self.freq_to_list[old_freq]) == 0:
            del self.freq_to_list[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1
        node.freq = new_freq
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        self._insert(new_freq, node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            old_freq = node.freq
            new_freq = old_freq + 1
            node.freq = new_freq
            self._remove(node)
            if len(self.freq_to_list[old_freq]) == 0:
                del self.freq_to_list[old_freq]
                if old_freq == self.min_freq:
                    self.min_freq = new_freq
            if new_freq not in self.freq_to_list:
                self.freq_to_list[new_freq] = DoublyLinkedList()
            self._insert(new_freq, node)
        else :
            if self.capacity == len(self.key_to_node):
                node = self.freq_to_list[self.min_freq].head.next
                self._remove(node)
                del self.key_to_node[node.key]
                if len(self.freq_to_list[node.freq]) == 0:
                    del self.freq_to_list[node.freq]
                newNode = Node(key, value)
                newNode.freq = 1
                if 1 not in self.freq_to_list:
                    self.freq_to_list[1] = DoublyLinkedList()
                self.min_freq = 1
                self._insert(1, newNode)
                self.key_to_node[key] = newNode
            else :
                newNode = Node(key, value)
                newNode.freq = 1
                if 1 not in self.freq_to_list:
                    self.freq_to_list[1] = DoublyLinkedList()
                self.min_freq = 1
                self._insert(1, newNode)
                self.key_to_node[key] = newNode



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)