class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # k = 3
        # 4 and 1
        # 10 and 7
        # k + 1
        if k == 0:
            return False
        
        seen = set()
        l = r = 0

        while r < len(nums):
            seen.add(nums[r])

            if (r - l + 1) < k + 1:
                if len(seen) < (r - l + 1):
                    return True

            if (r - l + 1) == k + 1:
                if len(seen) < (r - l + 1):
                    return True
                seen.remove(nums[l])
                l += 1
                
            r += 1 
        
        return False