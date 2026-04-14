class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int maxLen = 0;
        for(auto num: numSet){
            if(!numSet.count(num - 1)){
                int length = 1;
                int nextNum = num + 1;
                while(numSet.count(nextNum)){
                    length += 1;
                    nextNum += 1;
                }
                maxLen = max(maxLen, length);
            }
        }
        return maxLen;
    }
};
