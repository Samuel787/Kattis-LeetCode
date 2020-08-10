class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_set<char> data;
        int counter = 0;
        int max = 0;
        for(int i = 0; i < s.size(); i++){
            for(int j = i; j < s.size(); j++){
                if(data.find(s[j]) == data.end()){
                    counter++;
                    data.insert(s[j]);
                } else {
                    if(counter > max){
                        max = counter;
                    }
                    counter = 0;
                    data.clear();
                    break;
                }
                if(counter > max){
                    max = counter;
                }
            }
        }
        
        return max;
    }
};