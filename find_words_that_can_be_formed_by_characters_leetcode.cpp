class Solution {
public:
    vector<int> m;
    int countCharacters(vector<string>& words, string chars) {
        int count = 0;
        for(int i = 0; i < 26; i++){
            m.push_back(0);
        }
        for(char x : chars){
            m[x - 'a']++;
        }
        for(int i = 0; i < words.size(); i++){
            if(can_form(words[i])){
                count += words[i].size();
            }
        }
        return count;
    }
    
    bool can_form(string word){
        vector<int> c_map = m;
        for(char y: word){
            if(--c_map[y - 'a'] < 0){
                return false;
            }
        }
        return true;
    }
};