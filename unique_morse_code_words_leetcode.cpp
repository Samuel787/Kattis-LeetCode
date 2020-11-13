class Solution {
public:
    
    vector<string> CODES{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    
    int uniqueMorseRepresentations(vector<string>& words) {
        unordered_set<string> unique_morse_codes;
        for(string word : words){
            string morse_code = convert_to_morse_code(word);
            unique_morse_codes.insert(morse_code);
        }
        return unique_morse_codes.size();
    }
    
    string convert_to_morse_code(string word){
        string morse_code = "";
        for(char x : word){
            morse_code += CODES[x - 97];
        }
        return morse_code;
    }
};