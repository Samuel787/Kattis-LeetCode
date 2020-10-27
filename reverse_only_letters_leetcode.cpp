class Solution {
public:
    string reverseOnlyLetters(string S) {
        int backward_pointer = S.size() - 1;
        string result = "";
        for(int i = 0; i < S.size(); i++){
            if(is_letter(S[i])){
                // we can insert a letter here
                while(!is_letter(S[backward_pointer])){
                    backward_pointer--;
                }
                result += S[backward_pointer];
                backward_pointer--;
            } else {
                result += S[i];
            }
        }
        return result;
    }
    
    bool is_letter(char x){
        return ((x >= 65 && x <= 90) || (x >= 97 && x <= 122));
    }
};