from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for string in strs:
            keys["".join(sorted(string))].append(string)
        
        return list(keys.values())