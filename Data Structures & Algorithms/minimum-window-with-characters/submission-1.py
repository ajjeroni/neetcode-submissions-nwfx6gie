class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        window = {}
        have, need = 0, len(t_map)
        l = r = 0
        res, resLen = [-1,-1], float('inf')
        while r < len(s):
            if s[r] in t_map:
                window[s[r]] = window.get(s[r],0) + 1
            if s[r] in t_map and window.get(s[r],0) == t_map[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1
                if s[l] in window:
                    window[s[l]] -= 1
                if s[l] in t_map and window.get(s[l],0) < t_map[s[l]]:
                    have -= 1
                
                l += 1

            r += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""

        
        
                    

