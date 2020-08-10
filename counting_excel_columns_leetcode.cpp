class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        int counter = 0;
        for(int i = s.size() - 1; i >= 0; i--){
            result += (s[i] - 'A' + 1) * pow(26, counter);
            counter++;
        }
        return result;
    }
};