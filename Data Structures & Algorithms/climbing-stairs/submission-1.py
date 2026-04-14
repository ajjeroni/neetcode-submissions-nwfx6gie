class Solution:
    def climbStairs(self, n: int) -> int:
        #this will be a two branch recursion problem
        #one branch will check 1 step and the second will check 2 steps
        #base cases should return 1 or 0
        def step(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            return step(i + 1) + step(i + 2)
        return step(0)
        

        
