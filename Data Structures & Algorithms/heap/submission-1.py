class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        # bubble up
        self.heap.append(val)
        i = len(self.heap) - 1
        self._bubble_up(i)

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1

        # swap
        # bubble down
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(1)

        return res

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1

        return self.heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        for i in range(len(nums) // 2, 0, -1):
            self._bubble_down(i)

    def _bubble_down(self, index):
        i = index
        while i < len(self.heap):
            parent = self.heap[i]
            left = self.heap[i * 2] if i * 2 < len(self.heap) else float('inf')
            right = self.heap[i * 2 + 1] if i * 2 + 1 < len(self.heap) else float('inf')
            if parent <= left and parent <= right:
                return
            elif left <= right and parent > left:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            elif right < left and parent > right:
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
        
    def _bubble_up(self, index):
        parent = index // 2
        # parent is 0 -> index is 1
        # parent is 1 -> index is 2 or 3
        while parent >= 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = parent // 2







