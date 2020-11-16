class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        vector<string> result;
        if(A.size() == 0){
            return result;
        }
        vector<int> freq_count(26, INT_MAX);
        for(int i = 0; i < A.size(); i++){
            vector<int> current_count(26, 0);
            string current_string = A[i];
            for(int j = 0; j < current_string.size(); j++){
                current_count[current_string[j] - 'a']++;
            }
            for(int i = 0; i < 26; i++){
                freq_count[i] = min(freq_count[i], current_count[i]);
            }
        }
        
        for(int i = 0; i < 26; i++){
            for(int j = 0; j < freq_count[i]; j++){
                char x = i + 'a';
                // cout << x << endl;
                result.push_back({x});
            }
        }
        return result;
    }
};