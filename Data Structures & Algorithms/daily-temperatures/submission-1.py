class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonic decreasing stack
        ret = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                s_t, s_i = stack.pop()
                ret[s_i] = i - s_i
            stack.append((n, i))
        return ret