class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def test_minWeight(num: int) -> bool:
            count = 0
            numDays = 0
            for weight in weights:
                count += weight
                numDays += count // num
                
                if count > num:
                    count = weight
                elif count == num:
                    count = 0
                    
            numDays += math.ceil(count / num) 

            return numDays <= days
        
        l = max(weights)
        r = len(weights) * l
            
        while l < r:
            m = l + ((r - l) // 2)

            if test_minWeight(m):
                r = m
            else:
                l = m + 1
        
        return l
        
        

