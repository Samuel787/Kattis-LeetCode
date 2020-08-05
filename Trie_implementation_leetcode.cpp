class Trie {
public:
    /** Initialize your data structure here. */
    struct TrieNode{
        char c;
        unordered_map<char, TrieNode*> data;
        bool end = false;
    };
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        if(word.size() == 0) return;
        
        TrieNode* curr = root;
        for(int i = 0; i < word.size(); i++){
            char x = word[i];
            if((curr -> data)[x] == nullptr){
                TrieNode* newNode = new TrieNode();
                newNode -> c = x;
                if(i ==  word.size() - 1){
                    newNode -> end = true;
                }
                (curr -> data)[x] = newNode;
                curr = newNode;
            } else {
                curr = (curr -> data)[x];
                if(i == word.size() - 1){
                    curr -> end = true;
                }
            }
        }
        
        for(char x : word){
            if(curr -> data [x] == nullptr){
                TrieNode* newNode = new TrieNode();
                newNode -> c = x;
                
            }
        }
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* curr = root;
        for(int i = 0; i < word.size(); i++){
            char x = word[i];
            if((curr -> data)[x] == nullptr){
                return false;
            }
            curr = (curr -> data)[x];
            if(i == word.size() - 1){
                return curr -> end == true;
            }
        }
        return false; // by default
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* curr = root;
        for(int i = 0; i < prefix.size(); i++){
            char x = prefix[i];
            if((curr -> data)[x] == nullptr){
                return false;
            }
            curr = (curr -> data)[x];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */