class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, char> dict1;
        unordered_map<char, char> dict2;
        for (int i = 0; i < s.size(); i++) {
            if (dict1.find(s[i]) == dict1.end() || dict1[s[i]] == t[i]) {
                dict1[s[i]] = t[i];
            } else {
                return false;
            }
        }
        for (int i = 0; i < t.size(); i++) {
            if (dict2.find(t[i]) == dict2.end() || dict2[t[i]] == s[i]) {
                dict2[t[i]] = s[i];    
            } else {
                return false;
            }
        }
        for (auto& it: dict1) {
            if (it.first != dict2[dict1[it.first]]) {
                return false;
            }
        }
        return true;
        
    }
};
