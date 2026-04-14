class dNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = dNode(0,0)
        self.tail = dNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.remove_node(self.map[key])
        self.add_to_tail(self.map[key])

        return self.map[key].value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key, None)

        if node:
            node.value = value
            self.remove_node(node)
        else:
            node = dNode(key,value)
            self.map[key] = node
        
        if len(self.map) > self.capacity:
            lru = self.head.next
            self.remove_node(lru)
            del self.map[lru.key]
        
        self.add_to_tail(node)

    def remove_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev 
    
    def add_to_tail(self, node) -> None:
        prevNode = self.tail.prev

        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node