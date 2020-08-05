class MagicDictionary {
public:
    /** Initialize your data structure here. */
    unordered_map<int, vector<string>> data;
    MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        for(string x : dict){
            data[x.size()].push_back(x);
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        int length = word.size();
        for(string x: data[length]){
            int count = 0;
            for(int i = 0; i < x.size(); i++){
                if(x[i] != word[i]){
                    count++;
                }
            }
            if(count == 1) return true;
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary* obj = new MagicDictionary();
 * obj->buildDict(dict);
 * bool param_2 = obj->search(word);
 */