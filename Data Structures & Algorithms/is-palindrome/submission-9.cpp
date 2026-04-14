class Solution {
public:
    bool isPalindrome(string s) {
        int L = 0;
        int R = s.size() - 1;
        while(L < R){
            while(!isalnum(s[L]) && L < R){
                L += 1;
            }
            while(!isalnum(s[R]) && L < R){
                R -= 1;
            }
            if(tolower(s[L]) != tolower(s[R])){
                return false;
            }
            L += 1;
            R -= 1;
        }
        return true;
    }
};
