class Solution {
public:
    
    int longestPalindrome(string s) {
        unordered_map<char, int> data;
        for(char x : s){
            data[x]++;
        }
        
        int count = 0;
        
        //i sieve out all the even numbers first
        for(unordered_map<char, int>::iterator it = data.begin(); it != data.end(); it++){
            if(it -> second != 0 && it -> second % 2 == 0){
                count += (it -> second);
                it -> second = 0;
            } else if(it -> second > 1){
                count += it -> second - 1;
                it -> second = 1;
            }
            
            //other cases include 0 and 1
        }
        
        //check if there is one odd value left
        for(unordered_map<char, int>::iterator it = data.begin(); it != data.end(); it++){
            if(it-> second == 1){
                count += 1;
                break;
            }
            //other cases include 0 and 1
        }
        return count;
    }
};