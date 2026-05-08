class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can use hash set 
        # or hash map

        seen = set()
        L = R = 0
        lgSub = 0

        # dynamic sliding window 

        while R < len(s):
            
            # lets check if 
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            # lets add a char from the string one at a time
            seen.add(s[R])
            lgSub = max(lgSub, R - L + 1)
            R += 1
        
        return lgSub