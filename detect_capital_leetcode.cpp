class Solution {
public:
    
    bool allLower(string word){
        for(int i = 0; i < word.size(); i++){
            if(word[i] >= 'A' && word[i] <= 'Z'){
                return false;
            }
        }
        return true;
        
    }
    
    bool allUpper(string word){
        for(int i = 0; i < word.size(); i++){
            if(word[i] >= 'a' && word[i] <= 'z'){
                return false;
            }
        }
        return true;
    }
    
    bool onlyFirstUps(string word){
        int length = word.size();
        if(length == 0) return true;
        if((word[0] >= 'a' && word[0] <= 'z')){
            return false;
        }
        for(int i = 1; i < word.size(); i++){
            if(word[i] >= 'A' && word[i] <= 'Z'){
                return false;
            }
        }
        return true;
    }
    
    bool detectCapitalUse(string word) {
        return (allLower(word) || allUpper(word) || onlyFirstUps(word));
    }
};