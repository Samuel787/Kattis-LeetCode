class Solution {
public:
     
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_set<string> banned_words_set;
        for (int i = 0; i < banned.size(); i++) {
            banned_words_set.insert(banned[i]);
        }
        transform(paragraph.begin(), paragraph.end(), paragraph.begin(), ::tolower);
        vector<string> words = paragraph_to_string(paragraph);
        unordered_map<string, int> freq_table;
        for (int i = 0; i < words.size(); i++) {
            if (banned_words_set.find(words[i]) == banned_words_set.end()) {
                freq_table[words[i]]++;
            }
        }
        int max_count = 0;
        string max_word = "";
        for (auto& it : freq_table) {
            if (it.second >= max_count) {
                max_word = it.first;
                max_count = it.second;
            }
        }
        
        return max_word;
    }
    
    vector<string> paragraph_to_string(string paragraph) {
        int start = 0;
        vector<string> result;
        for (int i = 0; i < paragraph.size(); i++) {
            if (paragraph[i] == ' ' 
                || paragraph[i] == '?' 
                || paragraph[i] == '\'' 
                || paragraph[i] == ',' 
                || paragraph[i] == ';' 
                || paragraph[i] == '.'
                || paragraph[i] == '!') {
                if (start < i) {
                    result.push_back(paragraph.substr(start, i-start));
                }
                start = i + 1;
            }
        }
        if (start < paragraph.size()) {
            result.push_back(paragraph.substr(start, paragraph.size() - start));
        }
        return result;
    }
    
    void print_vector(vector<string> v) {
        for (string c : v) {
            cout << c << endl;
        }
    }
};