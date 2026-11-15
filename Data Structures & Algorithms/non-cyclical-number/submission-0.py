class Solution:
    def isHappy(self, n: int) -> bool:
        # its about floyd's cycle algorithm

        # lets define our test function
        def next_num(number):
            str_num = str(number)

            count = 0
            for char in str_num:
                num = int(char)
                count += num ** 2
            
            return count
        
        slow = fast = n
        while True:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

            if fast == 1:
                return True
            elif slow == fast:
                return False
