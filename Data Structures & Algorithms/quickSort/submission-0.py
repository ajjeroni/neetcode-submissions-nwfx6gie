# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) == 1 or not pairs:
            return pairs

        self.quickRec(0, len(pairs) - 1, pairs)
        return pairs

    def quickRec(self, s, e, pairs):
        if e - s + 1 <= 1:
            return 
        
        pivot = pairs[e]
        l = s
        for i in range(s, e):
            if pairs[i].key < pivot.key:
                # we swap
                pairs[l], pairs[i] = pairs[i], pairs[l]
                l += 1
        pairs[e], pairs[l] = pairs[l], pairs[e]

        self.quickRec(s, l - 1, pairs)
        self.quickRec(l + 1, e, pairs)



