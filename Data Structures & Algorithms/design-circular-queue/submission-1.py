class MyCircularQueue:

    def __init__(self, k: int):
        self.ringBuffer = [0] * k
        self.write = 0
        self.read = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.ringBuffer[self.write] = value
        self.write = (self.write + 1) % len(self.ringBuffer)        
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.read = (self.read + 1) % len(self.ringBuffer)
        self.size -= 1

        return True

    def Front(self) -> int:
        return self.ringBuffer[self.read] if not self.isEmpty() else -1 

    def Rear(self) -> int:
        return self.ringBuffer[self.write - 1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.ringBuffer)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()