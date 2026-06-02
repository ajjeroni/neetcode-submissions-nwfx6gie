class Solution:
    def trap(self, height: List[int]) -> int:
        summ = 0
        n = len(height)

        arr_left = [0] * n
        arr_right = [0] * n
        max_L = max_R = 0

        for i in range(n):
            j = -i -1

            arr_left[i] = max_L
            max_L = max(max_L, height[i])

            arr_right[j] = max_R
            max_R = max(max_R, height[j])

        for i in range(n):
            summ += max(0, min(arr_left[i], arr_right[i]) - height[i])

        return summ