class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result; 
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++){
            int comp = target - nums[i];
            if(mp.count(comp)){
                result.push_back(mp[comp]);
                result.push_back(i);
                return result;
            }else{
                mp[nums[i]] = i;
            }
        }
    }
};
