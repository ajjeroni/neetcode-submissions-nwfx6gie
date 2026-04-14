class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack - increasing 
        # traverse backwards 
        # tuple (temp, day)
        n = temperatures
        stack = []
        result = [0] * len(n)
        for i in range(len(n)-1,-1,-1):
            while stack and stack[-1][0] <= n[i]:
                stack.pop()
            result[i] = (stack[-1][1] - i) if stack else 0
            stack.append((n[i],i)) 
        return result