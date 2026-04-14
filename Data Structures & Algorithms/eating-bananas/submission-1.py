class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours








        l, r = 1, max(piles)
        k = max(piles)
        while l <= r:
            print('l:',l,',','r:',r)
            m = (l + r) // 2
            print('current k:', m)
            hours = eat(m)
            print("hours:", h)
            print("total hours:", hours)

            if h < hours:
                l = m + 1
                print('current k must increase')
            elif hours <= h:
                k = min(k, m)
                r = m - 1
                print('current k can decrease')
            print('/------------------/')
        return k