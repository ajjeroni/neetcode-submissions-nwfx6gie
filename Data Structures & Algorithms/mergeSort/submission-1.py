# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 1 or len(pairs) == 0:
            return pairs
        m = len(pairs) // 2
        lHalf = self.mergeSort(pairs[:m])
        rHalf = self.mergeSort(pairs[m:])
        return self.mergeProc(lHalf, rHalf)

    def mergeProc(self, lHalf, rHalf):
        sortedList = []
        l = r = 0

        while l < len(lHalf) and r < len(rHalf):
            if lHalf[l].key <= rHalf[r].key:
                sortedList.append(lHalf[l])
                l += 1
            else:
                # rHalf[r] < lHalf[l]
                sortedList.append(rHalf[r])
                r += 1

        while l < len(lHalf):
            sortedList.append(lHalf[l])
            l += 1
        while r < len(rHalf):
            sortedList.append(rHalf[r])
            r += 1

        return sortedList


