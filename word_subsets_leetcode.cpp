class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        vector<string> results;
        vector<int> char_count(26, 0);
        for(int i = 0; i < B.size(); i++){
            vector<int> temp_char_count = get_num_chars(B[i]);
            for(int j = 0; j < 26; j++){
                char_count[j] = max(char_count[j], temp_char_count[j]);
            }
        }
        
        for(int i = 0; i < A.size(); i++){
            vector<int> curr_char_count = get_num_chars(A[i]);
            bool is_valid = true;
            for(int j = 0; j < 26; j++){
                if(char_count[j] > curr_char_count[j]){
                    is_valid = false;
                    break;
                }
            }
            if(is_valid){
                results.push_back(A[i]);
            }
        }
        return results;
    }
    
    vector<int> get_num_chars(string x){
        //int char_count[26] = {0};
        vector<int> char_count(26, 0);
        for(char y: x){
            char_count[y-'a']++;
        }
        return char_count;
    }
};