class doubleNode():
    def __init__(self, key=0, val=0, next=None, behind=None):
        self.key = key
        self.val = val
        self.next = next
        self.behind = behind


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = doubleNode()
        self.tail = doubleNode(0,0,None,self.head)
        self.head.next = self.tail
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        toGet = self.cache[key]
        self.remove(toGet)
        self.use(toGet)
        return toGet.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            exists = self.cache[key]
            exists.val = value
            self.remove(exists)
            self.use(exists)
            return
        
        if len(self.cache) + 1 > self.capacity:
            toRemove = self.head.next
            del self.cache[toRemove.key]
            self.remove(toRemove)

        newNode = doubleNode(key,value)
        self.cache[key] = newNode
        self.use(newNode) 

        
    def use(self, node):
        before = self.tail.behind
        before.next = node 
        node.next = self.tail
        self.tail.behind = node 
        node.behind = before 
        
    def remove(self, node):
        before = node.behind
        after = node.next
        before.next = after
        after.behind = before











        
