class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        first create a dict with the freq of each num in nums
        you need an array of arrays to store the bucket 
        length of bucket array -> len(nums)
        based on the freq of the num, that index will hold that number
        iterate k times backwords in the bucket array
        we will append the numbers to a array we will return 
        '''
        freq = {} 
        for num in nums: #time O(N) - elements in nums
            freq[num] = freq.get(num, 0) + 1 #memory O(N) - freq has N key max
        print(freq)
        bucket = [[] for num in range(len(nums) + 1)] #memory O(N) - bucket has N arrays max
        for key, value in freq.items(): #time O(N) - freq has N keys max
            bucket[value].append(key) 
        print(bucket)
        arr = []
        #iterate k time from the end of an array 
        for i in range(len(bucket) - 1, 0, -1):
            for val in bucket[i]:
                arr.append(val)
            if len(arr) == k: 
                return arr
        
