'''
1. In the optimized approach, using normal head and tail pointer causes to have checks for conditions such as : no node, 1 node and 2 node.
2. If we use dummy nodes as head and tail pointer, all these checks can be avoided. The code will be clean and systematic.
3. Dummy boundary nodes handles all the following cases :
  - Empty list (head is None)
  - Single-node list (head is tail)
  - Removing the head node (no prev to update)
  - Removing the tail node (no next to update)
  - Moving the head node to tail.
4. With dummy boundary node with head and tail nodes always linked (head.next = tail, tail.prev = head), every real node is always 
positioned between these two nodes. So node.prev or node.next is never None for any real node. This makes code for insertion and deletion 
of nodes same for list of all sizes (0,1 or many real nodes.)
'''

class Node :
    def __init__(self, key=0 , value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # to store the address of key

        # dummy nodes for head and tail .i.e. dummy boundary nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        '''Removes an existing node from the linked list.'''
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous

    def _insert_at_end(self, node):
        '''Insert node immediately before the dummy tail.'''
        previous = self.tail.prev

        previous.next = node
        node.prev = previous

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # accessed node becomes most recently used.
        self._remove(node)
        self._insert_at_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # updating a key also makes it least recently used.
            self._remove(node)
            self._insert_at_end(node)
            return 

        if len(self.cache) == self.capacity:
            # the first node is the least recently used node.
            lru_node = self.head.next

            self._remove(lru_node)
            del self.cache[lru_node.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_at_end(new_node)


