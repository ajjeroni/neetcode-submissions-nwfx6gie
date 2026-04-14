class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sCarList = sorted(zip(position, speed), reverse=True)
        stack = [0]
        for p, s in sCarList:
            if stack[-1] < (target - p) / s:
                stack.append((target - p) / s)
                print(stack)
        return len(stack) - 1