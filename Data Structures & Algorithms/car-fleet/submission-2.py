class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []
        
        for i in range(len(cars)-1,-1,-1):
            time = (target - cars[i][0]) / cars[i][1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)
