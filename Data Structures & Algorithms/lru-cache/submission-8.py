class Node:
    def __init__(self, key=None, value=0, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.size = 0

        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        # moveToTail
        self.removeFromList(self.map[key])
        self.addToTail(self.map[key])

        return self.map[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            # moveToTail
            self.removeFromList(self.map[key])
            self.addToTail(self.map[key])
            return 
        
        if self.size == self.capacity:
            del self.map[self.head.next.key]
            self.removeFromList(self.head.next)
            self.size -= 1
            # removeLeast
        
        # addToTail
        node = Node(key, value)
        self.addToTail(node)
        self.map[key] = node
        self.size += 1

    def removeFromList(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    def addToTail(self, node):
        end = self.tail.prev
        end.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = end
    
    
        
        
        
    
