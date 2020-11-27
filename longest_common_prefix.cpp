class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string result = "";
        if(strs.size() == 0){
            return result;
        }
        for(int i = 0; i < INT_MAX; i++){
            bool same = true;
            char curr_char;
            if(strs[0].size() < (i + 1)){
                return result;
            } else {
                curr_char = strs[0][i];
            }
            for(int j = 1; j < strs.size(); j++){
                if(strs[j].size() < (i + 1)){
                    return result;
                } else if(strs[j][i] != curr_char){
                    same = false;
                    break;
                }
            }
            if(same){
                result += curr_char;
            } else {
                return result;
            }
        }
        return result;
    }
};