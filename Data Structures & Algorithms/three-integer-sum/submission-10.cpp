class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > 0){
                break;
            }
            if(0 < i && nums[i] == nums[i - 1]){
                continue;
            }
            int L = i + 1;
            int R = nums.size() - 1;
            int comp = 0 - nums[i]; 
            while(L < R){
                if(nums[L] + nums[R] < comp){
                    L ++;
                }else if(nums[L] + nums[R] > comp){
                    R --;
                }else{
                    ret.push_back({nums[i], nums[L], nums[R]});
                    L ++;
                    while(L < R && nums[L] == nums[L - 1]){
                        L ++;
                    }
                    R --;
                }
            }
        }
        return ret;
    }
};
