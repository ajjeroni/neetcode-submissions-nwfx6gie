class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(sM):
            l, r = 0, len(sM) - 1
            while l <= r:
                m = (l + r) // 2
                if target < sM[m]:
                    r = m - 1
                elif sM[m] < target:
                    l = m + 1
                else:
                    return True
            return False
        
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif matrix[mid][0] < target:
                if bs(matrix[mid]):
                    return True
                left = mid + 1
            else:
                return True
        return False