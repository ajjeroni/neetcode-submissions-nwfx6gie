class Solution {
public:
    int findMin(vector<int> &nums) {
        int res = nums[0];
        int L = 0;
        int R = nums.size() - 1;

        while(L <= R){
            if(nums[L] < nums[R]){
                res = min(res, nums[L]);
            }

            int M = (L + R) / 2;
            res = min(res, nums[M]);

            if(nums[L] <= nums[M]){
                L = M + 1;
            }else{
                R = M - 1;
            }
        }    

        return res;
    }
};
