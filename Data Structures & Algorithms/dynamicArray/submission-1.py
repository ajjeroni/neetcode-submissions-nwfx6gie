class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity
        self.count = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.array.append(n)
        self.count += 1
        if self.count > self.capacity:
            self.resize()

    def popback(self) -> int:
        self.count -= 1
        return self.array.pop()

    def resize(self) -> None:
        self.newArr = [0] * (self.capacity * 2)
        for i in range(len(self.array)):
            self.newArr[i] = self.array[i]
        self.capacity *= 2

    def getSize(self) -> int:
        return self.count

    def getCapacity(self) -> int:
        return self.capacity

