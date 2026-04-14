from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            groups[key].append(string)
        return list(groups.values())