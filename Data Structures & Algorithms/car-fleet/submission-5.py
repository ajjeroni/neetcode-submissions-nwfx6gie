class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        relDis = list(zip(position, speed))
        relDis.sort(reverse=True)

        stack = []
        for car in relDis:
            time = (target - car[0]) / car[1]

            if stack and stack[-1] >= time:
                continue
            stack.append(time)
            
        return len(stack)
            
