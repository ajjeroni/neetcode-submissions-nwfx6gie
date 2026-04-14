from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countStr = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord('a') - ord(char)] += 1
            countStr[tuple(count)].append(string)
        return list(countStr.values())