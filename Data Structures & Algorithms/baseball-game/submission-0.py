class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for op in operations:
            if op == 'C':
                nums.pop()
            elif op == 'D':
                nums.append(2 * int(nums[-1]))
            elif op == '+':
                nums.append(int(nums[-1]) + int(nums[-2]))
            else:
                nums.append(int(op))
        count = 0
        for num in nums:
            count += num

        return count