class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stk = []
        for i, n in enumerate(temperatures):
            while stk and stk[-1][0] < n:
                s_t, s_i = stk.pop()
                ret[s_i] = i - s_i
            stk.append((n, i))
        return ret