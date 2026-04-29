class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_before = 2
        two_step_before = 1

        for i in range(3, n + 1):
            curr = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = curr

        return one_step_before 