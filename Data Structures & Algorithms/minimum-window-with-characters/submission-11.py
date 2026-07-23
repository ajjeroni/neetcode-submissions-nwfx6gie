class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = r = 0
        length = float('inf')
        substring = [0,0]

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        have = 0
        need = len(count_t)
        window = {}

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while l <= r and have == need:
                if length > r - l + 1:
                    length = r - l + 1
                    substring = [l,r]

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

            r += 1

        if length == float('inf'):
            return ""

        l, r = substring
        return s[l:r + 1]





