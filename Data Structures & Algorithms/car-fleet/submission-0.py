class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sCarList = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in sCarList:
            if stack and stack[-1] >= (target - p) / s:
                continue
            else:
                stack.append((target - p) / s)
        return len(stack)