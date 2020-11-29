class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        // string no_dash = "";
        S = toupper_(S);
        queue<char> no_dash;
        for(int i = 0; i < S.size(); i++){
            if(S[i] != '-'){
                no_dash.push(S[i]);
            }
        }
        int length = no_dash.size();
        int remainder = length % K;
        string result = "";
        for(int i = 0; (i < remainder && !no_dash.empty()); i++){
            result += no_dash.front();
            no_dash.pop();
        }
        int counter = 0;
        while(!no_dash.empty()){
            if(counter % K == 0 && result != ""){
                result += '-';
            }
            result += no_dash.front();
            no_dash.pop();
            counter++;
        }
        return result;
    }
    
    string toupper_(string word){
        for(int i = 0; i < word.size(); i++){
            if(word[i] != '-'){
                word[i] = toupper(word[i]);
            }
        }
        return word;
    }
};