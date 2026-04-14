class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // [1, 2, 4, 6]
        // [1, 1, 1, 1]
        // [1, 1, 2, 8]
        // [48, 24, 6, 1]
        // [48, 24, 12, 8]
        vector<int> res(nums.size(), 1);
        int post = 1;
        for(int i = res.size()-1; i >= 0; i--){
            res[i] = post;
            post *= nums[i];
        }
        int pre = 1;
        for(int i = 0; i < res.size(); i++){
            res[i] *= pre;
            pre *= nums[i];
        }

        return res;
    }
};
