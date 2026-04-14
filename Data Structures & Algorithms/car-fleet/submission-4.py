class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        highway = list(zip(position, speed))
        highway = sorted(highway)
        print(highway)
        see = []
        for pos,spd in highway:
            time = (target - pos) / spd
            see.append(time)
        print(see)
        stack = []
        for i in range(len(highway)-1,-1,-1):
            time = (target - highway[i][0]) / highway[i][1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
            print(stack)
        return len(stack)
            