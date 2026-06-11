from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for string in strs:
            id_ = [0] * 26
            for char in string:
                id_[ord(char) - ord('a')] += 1
            keys[tuple(id_)].append(string)

        return list(keys.values())