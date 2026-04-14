class Solution {
public:
    int trap(vector<int>& height) {
        int L = 0;
        int maxL = height[L];
        int R = height.size() - 1;
        int maxR = height[R];
        int tWater = 0;
        while(L < R){
            if (height[L] <= height[R]){
                ++L;
                maxL = max(maxL, height[L]);
                tWater += maxL - height[L];
            }else{
                --R;
                maxR = max(maxR, height[R]);
                tWater += maxR - height[R];
            }
        }
        return tWater;
    }
};
