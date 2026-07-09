class ListNode:

    def __init__(self, key: int, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    # chaining
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [ListNode(0) for i in range(capacity)]

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        curr = self.table[index]

        while curr.next:
            curr = curr.next
            if curr.key == key:
                curr.value = value
                return
        self.size += 1
        curr.next = ListNode(key, value)

        if self.size * 2 >= self.capacity:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity
        curr = self.table[index]

        while curr.next:
            curr = curr.next
            if curr.key == key:
                return curr.value

        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        curr = self.table[index]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -= 1
                return True
            curr = curr.next
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_table = self.table
        old_capacity = self.capacity

        self.capacity *= 2
        self.table = [ListNode(0) for i in range(self.capacity)]

        old_size = self.size
        self.size = 0

        for i in range(old_capacity):
            curr = old_table[i].next

            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next

        self.size = old_size
