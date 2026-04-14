class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lane = sorted(zip(position,speed))
        stack = []
        # monotic increasing
        for i in range(len(lane)-1,-1,-1):
            time = (target - lane[i][0]) / lane[i][1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)
        