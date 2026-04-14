class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        window,countT = {},{}
        for c in t:
            countT[c] = countT.get(c,0) + 1
        l = r = 0
        have,need = 0,len(countT)
        res,resLen = [-1,-1],float('inf')
        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            r += 1
        i,j = res
        return s[i:j+1] if resLen > 0 else ""












