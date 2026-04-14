class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        temp = temperatures
        result = [0] * len(temp)
        stack = []
        for i in range(len(temp)-1,-1,-1):
            while stack and stack[-1][0] <= temp[i]:
                stack.pop()
            result[i] = stack[-1][1] - i if stack else 0
            stack.append((temp[i],i))
        return result