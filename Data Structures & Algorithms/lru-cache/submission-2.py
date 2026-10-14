class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def insert(self, node): 
        self.head.nxt.prev = node
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt = node
    
    def remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        capacity = len(self.cache)

        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = newNode
            self.insert(newNode)
        
        else:
            while capacity >= self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
                capacity = len(self.cache)

            self.cache[key] = newNode
            self.insert(newNode)







