class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freq;
        int L = 0;
        int maxF = 0;
        int res = 0;
        for(int R = 0; R < s.size(); R++){
            freq[s[R]] += 1;
            maxF = max(maxF, freq[s[R]]);
            while((R - L + 1) - maxF > k){
                freq[s[L]] -= 1;
                L ++;
            }
            res = max(res, R - L + 1);
        }
        return res;
    }
};
