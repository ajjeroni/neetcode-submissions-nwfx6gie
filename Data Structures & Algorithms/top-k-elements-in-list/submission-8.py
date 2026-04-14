class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #i assume the question is asking to return the same array
        #where the number(k) of most frequent elements in that array
        '''
        are at the 'front' or [0, k) indexes 
        how am i going to implement this?
        well is the nums array in non-descending order? any order in
        particular?
        
        Maybe create a dict of nums and count the frequency for 
        each integer
        create an array that will hold the max freq
        And then iterate through that dict k times and 
        find the max values each time 
        then delete that key-value pair from the dict 
        once the iteration is done
        somehow place the new array at the beginning of nums
        '''
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1
        print(numsDict)
        arr = []
        for i in range(k):
            maxVal = 0
            maxKey = 0
            for key in numsDict:
                print("current key: ", key, "value :", numsDict[key])
                if numsDict[key] > maxKey:
                    maxVal = key
                    maxKey = numsDict[key]
                    print("New Max:", maxVal)
            print("maxVal:", maxVal)
            arr.append(maxVal) 
            del numsDict[maxVal]
            
        return arr







