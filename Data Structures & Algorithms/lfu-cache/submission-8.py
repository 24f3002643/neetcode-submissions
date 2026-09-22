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
    # Optimized approach
    # I will use double linked list, with 3 fields : key, value, count.
    # Also, a dict will be used to store the addresses of these nodes
    # When a key will be accessed, the count will be incremented, and it will be removed and added at last
    # For put, if a key exist, we increment the count, remove the node and append  it at last.
    # for put, if key does not exist, we append te node at last.
    # now, in this way, the node at last will always have maximum count.
    # so for put, if capacity is full, we remove the node at head.
    #  So in case of tie, removing the node at head means removing the node with least count, and also least used.
    # In this way, we get combo of both LRU and LFU.

    # Analysis of Above apporach 
    
    # The above analysis is wrong.
    # Recency and frequency are two independent axis.
    # Suppose key 1 was accessed 10 times, and then key 2 and key 3 was added.
    # In the above case, the list would be : 1 -> 2 -> 3
    # Now for eviction, key 1 would be selected, which was actually most frequently used.
    # using a linked list, the head node only tells about recency, not frequency.
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
        new_freq = node.freq + 1
        self._remove(node)
        if len(self.freq_to_list[old_freq]) == 0:
            del self.freq_to_list[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1
        # In the above lines, the core idea of checking if that current list becomes empty is :
        # we only increment the min_freq when two conditions are satisfied :
        # 1. the list belong to min_freq, and 
        # 2. now it has no element when the node is removed i.e. list became empty
        # it may happen, that a list with higher freq became empty, so in that cas, min_freq need not be updated.
        node.freq += 1
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        self._insert(new_freq, node)
        return self.key_to_node[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            if self.capacity == len(self.key_to_node):
                node = self.freq_to_list[self.min_freq].head.next
                del self.key_to_node[node.key]
                self._remove(node)
                if len(self.freq_to_list[node.freq]) == 0:
                    del self.freq_to_list[node.freq] # since doubleLinkedList is empty
            newNode = Node(key, value)
            newNode.freq = 1
            self.key_to_node[key] = newNode
            if 1 not in self.freq_to_list:
                self.freq_to_list[1] = DoublyLinkedList()
            self._insert(newNode.freq, newNode)
            self.min_freq = 1
        else:
            node = self.key_to_node[key]
            node.value = value
            old_freq = node.freq
            new_freq = old_freq + 1
            node.freq += 1
            self._remove(node)
            if len(self.freq_to_list[old_freq]) == 0:
                del self.freq_to_list[old_freq]
                if old_freq == self.min_freq:
                    self.min_freq += 1
            if node.freq not in self.freq_to_list:
                self.freq_to_list[node.freq] = DoublyLinkedList()
            self._insert(node.freq, node)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)