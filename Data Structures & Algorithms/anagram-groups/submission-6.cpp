class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> groups;
        for(string str: strs){
            int count[26] = {0}; 
            for(char c: str){
                count[c - 'a'] += 1;
            }
            string id;
            for(int v: count){
                id += to_string(v) + '#';
            }
            for(char d: id){
                std::cout<<d;
            }
            std::cout<<endl;
            groups[id].push_back(str);
        }
        vector<vector<string>> ret; 
        for(auto val: groups){
            ret.push_back(val.second);
        }
        return ret;
    }
};
