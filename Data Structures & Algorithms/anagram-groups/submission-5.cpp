class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> groups;
        for(string word : strs){
            vector<int> count(26, 0);
            for(char letter : word){
                count[letter - 'a']++;
            }
            string key;
            for (int num: count){
                key += to_string(num) + ',';
            }
            std:: cout<< key << endl;
            groups[key].push_back(word);
        }
        for(auto& group : groups){
            res.push_back(group.second);
        }
        return res;
    }
};
