class MyQueue:

    def __init__(self):
        self.stackpop = []
        self.stackpush = []

    def push(self, x: int) -> None:
        self.stackpush.append(x)

    def pop(self) -> int:
        if not self.stackpop:
            while self.stackpush:
                self.stackpop.append(self.stackpush.pop())

        return self.stackpop.pop()

    def peek(self) -> int:
        if not self.stackpop:
            return self.stackpush[0]
        return self.stackpop[-1]

    def empty(self) -> bool:
        return len(self.stackpop) == 0 and len(self.stackpush) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()