from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.lists = defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.maxCount = max(self.maxCount, self.freq[val])
        self.lists[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.lists[self.maxCount].pop()
        self.freq[val] -= 1
        self.maxCount = self.maxCount if self.lists[self.maxCount] else self.maxCount - 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()