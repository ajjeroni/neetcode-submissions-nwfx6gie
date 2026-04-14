class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        # O(n) since it will hold n + 1 lists in that array
        freq = {}
        # O(n) since it will hold n elements as keys in the worst scenerio 
        for num in nums: 
            #O(n) 
            freq[num] = freq.get(num, 0 ) + 1
            #O(1)
        
        for num in freq:
            #O(n) at worst
            buckets[freq[num]].append(num)
        
        ret = []
        #O(k) 
        print(buckets)
        for i in range(len(nums), 0 , -1):
            print(buckets[i])
            for num in buckets[i]:
                print(ret)
                if len(ret) == k:
                    return ret
                ret.append(num)
                
        return ret
            
    
