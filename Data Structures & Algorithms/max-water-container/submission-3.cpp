class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxCon = 0;
        int L = 0;
        int R = heights.size() - 1;
        while(L < R){
            int con = min(heights[L], heights[R]) * (R - L);
            maxCon = max(maxCon, con);
            if(heights[L] < heights[R]){
                L ++;
            }else if(heights[L] >= heights[R]){
                R --;
            }
        }
        return maxCon;
    }
};
