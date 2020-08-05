class WordDictionary {
public:
    
    unordered_map<int, vector<string>> data;
    /** Initialize your data structure here. */
    WordDictionary() {
        
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        data[word.size()].push_back(word);
    }
    
    bool compare_words(string word1, string word2){
        for(int i = 0; i < word1.size(); i++){
            if(word2[i] != '.' && word1[i] != word2[i]){
                return false;
            }
        }
        return true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        int length = word.size();
        for(int i = 0; i < data[length].size(); i++){
            if(compare_words(data[length][i], word)){
                return true;
            }
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */