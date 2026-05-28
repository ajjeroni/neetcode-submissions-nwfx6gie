from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # [10] -> 1
        if key not in self.storage:
            return ""
        
        l, r = 0, len(self.storage[key]) - 1
        while l < r:
            m = l + (r - l) // 2 + 1
            if self.storage[key][m][1] <= timestamp:
                l = m
            else:
                r = m - 1
        
        return self.storage[key][l][0] if self.storage[key][l][1] <= timestamp else ""
