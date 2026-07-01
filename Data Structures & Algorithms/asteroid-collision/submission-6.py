class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:

            if num < 0:
                if stack and ((stack[-1] ^ num) >= 0):
                    stack.append(num)
                elif stack and ((stack[-1] ^ num) < 0) and stack[-1] == abs(num):
                    stack.pop()
                else:
                    while stack and ((stack[-1] ^ num) < 0) and stack[-1] < abs(num):
                        stack.pop()
                    if stack and stack[-1] == abs(num):
                        stack.pop()
                    elif not stack:
                        stack.append(num)
                    elif stack and ((stack[-1] ^ num) >= 0):
                        stack.append(num)
            else: 
                stack.append(num)
                
        return stack