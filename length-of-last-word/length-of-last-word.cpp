class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        if(s.size() == 0){
            return length;
        }
        bool gotSpace = false;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == ' '){
                gotSpace = true;
            } else {
                if(gotSpace){
                    length = 0;
                }
                gotSpace = false;
                length++;
            }
        }
        return length;
    }
};