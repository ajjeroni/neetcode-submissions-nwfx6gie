class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return len(nums)

        seen = set(nums)
        lg_chain = 0

        for i,num in enumerate(nums):
            if (num - 1) in seen:
                continue
            
            next_num = num + 1
            curr_chain = 1
            while next_num in seen:
                curr_chain += 1
                next_num += 1

            lg_chain = max(lg_chain, curr_chain)

        return lg_chain   
    
