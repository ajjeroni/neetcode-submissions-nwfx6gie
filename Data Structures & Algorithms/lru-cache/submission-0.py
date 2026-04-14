class DoublyLinkedNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoublyLinkedNode(0,0)
        self.tail = DoublyLinkedNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return self.hashmap[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])

        node = DoublyLinkedNode(key,value)
        self.hashmap[key] = node

        if len(self.hashmap) > self.capacity:
            toRemove = self.head.next
            del self.hashmap[toRemove.key]
            self.remove_node(toRemove)
        
        self.add_to_tail(node)

    def remove_node(self, node: DoublyLinkedNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev 
    
    def add_to_tail(self, node: DoublyLinkedNode) -> None:
        prevNode = self.tail.prev

        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node 



