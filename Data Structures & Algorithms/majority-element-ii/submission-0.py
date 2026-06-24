class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        print(n)
        res = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        print(freq)
        for num,count in freq.items():
            print(num, count)
            if count > n:
                res.append(num)
        return res