class Solution {
public:
    // unordered_map<char, int> data
    bool isAnagram(string s, vector<int> char_counts){
        for(int i = 0; i < s.size(); i++){
            if(char_counts[s[i] - 'a'] == 0){
                return false;
            } else {
                char_counts[s[i] - 'a']--;
            }
        }
        return true;
    }
    
    vector<int> findAnagrams(string s, string p) {
        vector<int> results;
        //unordered_map<char, int> data;
        //int char_counts[26];
        vector<int> char_counts(26, 0);
        for(int i = 0; i < p.size(); i++){
            //data[p[i]]++;
            char_counts[p[i] - 'a']++;
        }
        
        for(int i = 0; i < s.size() - p.size() + 1; i++){
            //check the window
            if(i + p.size() > s.size()){
                break;
            }
            
            if(isAnagram(s.substr(i, p.size()), char_counts)){
                results.push_back(i);
                //quick check next window
                while(i < s.size() - p.size() + 1 && i + p.size() > s.size() && s[i] == s[i +p.size()]){
                    results.push_back(i+1);
                    i++;
                }
            }
        }
        return results;
    }
};