class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        map<char, int> literals;
        
        literals['I'] = 1;
        literals['V'] = 5;
        literals['X'] = 10;
        literals['L'] = 50;
        literals['C'] = 100;
        literals['D'] = 500;
        literals['M'] = 1000;
        
        int prev = 0;
        for(int i = s.size() - 1; i >= 0; i--){
            if(literals[s[i]] >= prev){
                result += literals[s[i]]; 
                prev = literals[s[i]];
            } else {
                result -= literals[s[i]];
            }
        }
        cout << result << endl;
        
        return result;
    }
};