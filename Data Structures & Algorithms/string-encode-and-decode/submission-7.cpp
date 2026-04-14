class Solution {
public:
    string encode(vector<string>& strs) {
        string res;
        for(auto word:strs){
            res += to_string(word.size()) + '#' + word;
        }
        std::cout<<res;
        return res;
    }

    vector<string> decode(string s) {
        int L = 0;
        vector<string> res;
        while(L < s.size()){
            int R = L;
            while(s[R] != '#'){
                R += 1;
            }
            int length = stoi(s.substr(L, R));
            res.push_back(s.substr(R + 1, length));
            L = R + 1 + length;
        }
        return res;
    }
};
