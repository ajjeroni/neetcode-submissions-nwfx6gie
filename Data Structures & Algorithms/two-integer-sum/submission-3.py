class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #first you create the data structure that will hold your key-value pairs
        #why a dictionary?
        #because I want to iterate through the nums array,
        #each iteration will subtract the target minus the current element/int
        #this will give us a value/key to find in the dictionary
        #the value for that key will hold the index we need 
        #we return the current element/int index and the index from the key/value

        numDict = {}
        for i, n in enumerate(nums):
            pair = target - n 
            if pair in numDict:
                return [numDict[pair], i]
            numDict[n] = i
        
                