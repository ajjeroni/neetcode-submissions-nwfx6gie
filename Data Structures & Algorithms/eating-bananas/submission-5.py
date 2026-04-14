class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def does_k_work(m):
            total = 0
            for b in piles:
                total += math.ceil(b / m)
            return True if total <= h else False
        l,r = 1,max(piles)
        # test = []
        # for i in range(l, r + 1):
        #     test.append(does_k_work(i))
        # print(test)
        while l < r:
            m = (l + r) // 2
            if not does_k_work(m):
                l = m + 1
            else:
                r = m
        return r