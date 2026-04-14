class Solution {
public:
    string encode(vector<string>& strs) {
        string ret; 
        for(string str: strs){
            ret += to_string(str.size()) + '#' + str;
        }
        return ret;
    }
    vector<string> decode(string s) {
        vector<string> ret;
        int L = 0;
        while(L < s.size()){
            int R = L;
            while(s[R] != '#'){
                R += 1;
            }
            int length = stoi(s.substr(L, R - L));
            ret.push_back(s.substr(R + 1, length));
            L = R + 1 + length;
        }
        return ret;
    }
};
