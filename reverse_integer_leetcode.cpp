#include <bits/stdc++.h>
using namespace std;

    int reverse(int x) {
        bool is_negative = false;
        if(x < 0){
            is_negative = true;
            x *= -1;
        }
        int length = (to_string(x)).length();
        int new_number = 0;
        for(int i = 1; i < length; i++){
            int digit = 
        }
    }


int main(){
    int x = 2147483647;
    cout << reverse(x) << endl;

}class Solution {
public:
    int reverse(int x) {
        bool is_negative = false;
        if(x < 0)
            is_negative = true;
        string number = to_string(x);
        string new_number = "";
        for(int i = number.length()-1; i >= 0; i--){
            if(number[i] != '-')
                new_number += number[i];
        }
        int count = 0;
        while(new_number[count] == '0'){
            new_number = new_number.substr(count, new_number.length());
            count++;
        }
        long long n = stoll(new_number);
        if(is_negative)
            n *= -1;
        if(n > 2147483647 || n < -2147483648){
            return 0;
        }
        return n;
    }
};