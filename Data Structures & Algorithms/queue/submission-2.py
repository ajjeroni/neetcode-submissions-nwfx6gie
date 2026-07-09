class ListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
class Deque:
    def __init__(self):
        # skrew it lets do circular array
        # after dlinkedlist lol
        self.length = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def append(self, value: int) -> None:
        #
        left = self.tail.prev
        right = self.tail
        newNode = ListNode(value)
        
        left.next = newNode
        newNode.next = right

        right.prev = newNode
        newNode.prev = left

        self.length += 1

    def appendleft(self, value: int) -> None:
        #
        left = self.head
        right = self.head.next
        newNode = ListNode(value)

        left.next = newNode
        newNode.next = right
        
        right.prev = newNode
        newNode.prev = left

        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return -1
        
        res = self.tail.prev.value
        
        #
        left = self.tail.prev.prev
        right = self.tail

        left.next = right
        right.prev = left

        
        self.length -= 1    

        return res
        
    def popleft(self) -> int:
        if self.length == 0:
            return -1
        
        res = self.head.next.value
        
        #
        left = self.head
        right = self.head.next.next

        left.next = right
        right.prev = left

        self.length -= 1

        return res
