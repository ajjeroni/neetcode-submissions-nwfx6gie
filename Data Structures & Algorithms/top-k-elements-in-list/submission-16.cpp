class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> buckets[nums.size() + 1];
        unordered_map<int, int> freq;
        for(auto num : nums){
            freq[num] += 1;
        }
        for(auto pair: freq){
            buckets[pair.second].push_back(pair.first);
        }
        vector<int> res;
        for(int i = nums.size(); i > 0; i--){
            for(int j = 0; j < buckets[i].size(); j++){
                res.push_back(buckets[i][j]);
                if(res.size() == k){
                    return res;
                }
            }
        }
    }
};
