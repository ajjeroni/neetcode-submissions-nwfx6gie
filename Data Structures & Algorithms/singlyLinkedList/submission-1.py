class listNode:
    def __init__(self, value=0, nxt=None):
        self.value = value
        self.next = nxt

class LinkedList:    
    def __init__(self):
        self.root = self.tail = listNode()
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.root.next
        for i in range(index): 
            curr = curr.next

        return curr.value

    def insertHead(self, val: int) -> None:
        currHead = self.root.next
        self.root.next = listNode(val)
        self.root.next.next = currHead
        self.length += 1

        while self.tail.next:
            self.tail = self.tail.next


    def insertTail(self, val: int) -> None:
        self.tail.next = listNode(val)
        self.tail = self.tail.next
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        
        curr = self.root
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next

        if not curr.next:
            self.tail = curr

        self.length -= 1

        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.root.next
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
