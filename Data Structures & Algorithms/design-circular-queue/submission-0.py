class ListNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.back = ListNode()

        while k > 1:
            nextNode = ListNode()
            self.back.next = nextNode
            nextNode.prev = self.back
            self.back = self.back.next    
            k -= 1
        
        self.back.next = self.front
        self.front.prev = self.back
        self.back = self.front
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.back.value = value
        self.back = self.back.next

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.front.value = None
        self.front = self.front.next

        return True

    def Front(self) -> int:
        return self.front.value if not self.isEmpty() else -1 

    def Rear(self) -> int:
        return self.back.prev.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return True if self.front == self.back and not self.front.value else False 

    def isFull(self) -> bool:
        return True if self.front == self.back and self.front.value else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()