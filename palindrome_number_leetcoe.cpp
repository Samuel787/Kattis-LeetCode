#include <bits/stdc++.h>
using namespace std;

    bool isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        string number = to_string(x);
        int low = 0;
        int high = number.length()-1;
        while(low < high){
            if(low ==  high){
                return true;
            } else {
                if(number[low] == number[high]){
                    low++;
                    high--;
                    continue;
                }
                else
                    return false;
            }
        }
        return true;
    }

    /*
    driver code
    */
    
int main(){
    int x = 121;
    cout << isPalindrome(x) << endl;
}