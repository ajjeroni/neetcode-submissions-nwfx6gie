class Solution:

    def encode(self, strs: List[str]) -> str:
        #outputs a long singular string composed of all strings in strs
        #"neetcodeloveyou"
        # result = ''
        # for string in strs:
            # result += str(len(string)) + '#'
            # for char in string:
            #     result += char
        # return result
        if not strs:
            return "ññ" 

        return ("ñ").join(strs)
        
        #"4#neet4#code4#love3#you"
    def decode(self, s: str) -> List[str]:
        #input
        #puts the output of encode back to the list strs 
        # result = []
        # for i in range(len(s)):
        #     if s[i].isnumeric() and s[i + 1] == '#':
        #         s.split
        if s == "ññ":
            return []
        print(s)
        if not s:
            return [""]
        
        

        return(s.split("ñ")) 
        
