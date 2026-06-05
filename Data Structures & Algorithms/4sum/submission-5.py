class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

        for a,num_a in enumerate(nums):
            
            # if num_a > target:
            #     break 

            if a > 0 and num_a == nums[a - 1]:
                continue

            targ_a = target - num_a
            print('targ_a:',targ_a)
            print('a:', num_a)

            for b in range(a + 1, len(nums)):

                num_b = nums[b]

                # if num_b > targ_a:
                #     break

                if b > a + 1 and num_b == nums[b - 1]:
                    continue

                targ_b = targ_a - num_b
                
                print('     targ_b:',targ_b)
                print('     b:', num_b)

                l, r = b + 1, len(nums) - 1

                while l < r:

                    num_c = nums[l]
                    num_d = nums[r]
                    print('         c:', num_c)
                    print('         d:', num_d)
                    summ = num_c + num_d

                    if summ == targ_b:
                        res.append([num_a,num_b,num_c,num_d])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                    elif summ < targ_b:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        r -= 1
        return res
                    
                











