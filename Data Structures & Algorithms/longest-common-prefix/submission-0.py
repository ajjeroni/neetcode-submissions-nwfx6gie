class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = []

        for i in range(len(strs[0])):
            for string in strs:
                if i >= len(string) or string[i] != strs[0][i]:
                    return "".join(prefix)
            prefix.append(strs[0][i])

        return "".join(prefix)