class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        res = [0] * len(temps)
        stack = []
        
        for i,num in enumerate(temps):
            while stack and stack[-1][0] < num:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append((num, i))
        return res
            