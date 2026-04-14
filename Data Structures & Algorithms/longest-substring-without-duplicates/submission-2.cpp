class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> c;
        int lg = 0;
        int L = 0;
        for(int R = 0; R < s.size(); R++){
            while(c.count(s[R])){
                c.erase(s[L]);
                L ++;
            }
            c.insert(s[R]);
            lg = max(lg, R - L + 1);
        }
        return lg;
    }
};
