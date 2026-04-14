class dNode:
    def __init__(self, key=-1, val=0):
        self.key = key
        self.val = val
        self.nxt = self.prv = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}
        self.tail = dNode()
        self.head = dNode()
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def get(self, key: int) -> int:
        # access map first 
        if key not in self.keyMap:
            return -1
        
        # if key exists return value and move to the right
        node = self.keyMap[key]
        self.removeNode(node)
        self.addToTail(node)

        return self.keyMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            self.removeNode(self.keyMap[key])
        
        # add the left of tail 
        node = dNode(key,value)
        self.keyMap[key] = node
        # if there are more keys than capacity
        if len(self.keyMap) > self.capacity:
            lru = self.head.nxt
            self.removeNode(lru)
            del self.keyMap[lru.key]
        # remove from right of head
        self.addToTail(node)

    def removeNode(self, node: dNode):
        node.nxt.prv = node.prv
        node.prv.nxt = node.nxt
    
    def addToTail(self, add):
        node = self.tail.prv

        node.nxt = add
        add.nxt = self.tail
        self.tail.prv = add
        add.prv = node