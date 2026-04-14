from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c)-ord('a')] += 1
            keys[tuple(key)].append(string)
        return list(keys.values())