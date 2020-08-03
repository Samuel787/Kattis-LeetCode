class Solution {
public:
    
    string stripString(string input){
        string new_string = "";
        int diff = 'a' - 'A';
        for(int i = 0; i < input.size(); i++){
            if(input[i] >= 'a' && input[i] <= 'z'){
                new_string += input[i];
            } else if(input[i] >= 'A' && input[i] <= 'Z'){
                new_string += input[i] + diff; 
            } else if(input[i] >= '0' && input[i] <= '9'){
                new_string += input[i];
            }
        }
        cout << new_string << endl;
        return new_string;
    }
    bool isPalindrome(string s) {
        
        if(s == "") return true;
        
        s = stripString(s);
        int start = 0;
        int end = s.size() - 1;
        while(start < end){
            if(s[start] != s[end]){
                cout << "start: " << s[start] << " end: " << s[end] << endl;
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};