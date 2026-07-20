from collections import defaultdict

class Node:
    def __init__(self, key=None, value=0, freq=1, next=None, prev=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = next
        self.prev = prev

class NodeList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.keyToNode = {}
        self.length = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeRight(self, node):
        before = self.tail.prev

        before.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = before

        self.keyToNode[node.key] = node
        self.length += 1

    def removeNode(self, key):
        node = self.keyToNode[key]
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

        del self.keyToNode[key]
        self.length -= 1

        return node

    def lfuRemove(self):
        if self.length == 0:
            return

        node = self.head.next

        self.head.next = node.next
        node.next.prev = self.head

        del self.keyToNode[node.key]
        self.length -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freqToList = defaultdict(NodeList)
        self.keyToFreq = defaultdict(int)
        self.lfuCount = 0
        self.size = 0

    def _count(self, oldFreq, oldList):
        if oldFreq == self.lfuCount and oldList.length == 0:
            self.lfuCount += 1
        

    def get(self, key: int) -> int:
        if key in self.keyToFreq:
            freq = self.keyToFreq[key]
            freqList = self.freqToList[freq]
            node = freqList.removeNode(key)

            self._count(freq, freqList)

            self.keyToFreq[key] += 1
            freq = self.keyToFreq[key]
            freqList = self.freqToList[freq]
            freqList.addNodeRight(node)

            return node.value

        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.keyToFreq:
            freq = self.keyToFreq[key]
            freqList = self.freqToList[freq]
            node = freqList.removeNode(key)
            node.value = value

            self._count(freq, freqList)

            self.keyToFreq[key] += 1
            freq = self.keyToFreq[key]
            freqList = self.freqToList[freq]
            freqList.addNodeRight(node)

            return

        if self.capacity == self.size:
            freqList = self.freqToList[self.lfuCount]
            del self.keyToFreq[freqList.head.next.key]
            node = freqList.lfuRemove()
            self.size -= 1
            
        
        node = Node(key, value)
        self.freqToList[1].addNodeRight(node)
        self.keyToFreq[key] = 1
        self.lfuCount = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)