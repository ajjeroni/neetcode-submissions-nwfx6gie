class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int L = 0;
        int maxProf = 0;
        for(int R = 0; R < prices.size(); R++){
            if(prices[L] >= prices[R]){
                L = R;
            }else{
                int prof = prices[R] - prices[L];
                maxProf = max(maxProf, prof);
            }
        }
        return maxProf;
    }
};
