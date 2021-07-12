class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> dict1;
        unordered_map<char, int> dict2;
        for (int i = 0; i < s.size(); i++) {
            if ((dict1.find(s[i]) != dict1.end() && dict2.find(t[i]) != dict2.end()
               && dict1[s[i]] == dict2[t[i]]) || (dict1.find(s[i]) == dict1.end() && dict2.find(t[i]) == dict2.end())) {
                dict1[s[i]] = i;
                dict2[t[i]] = i;
            } else {
                return false;   
            }
        }
        return true;
    }
};
