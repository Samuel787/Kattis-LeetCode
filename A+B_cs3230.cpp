#include <bits/stdc++.h>
using namespace std;

int main(){
    string A, B;
    cin >> A;
    cin >> B;
    
    string result = "";
    int pointer_a = A.size() - 1;
    int pointer_b = B.size() - 1;
    queue<char> temp;
    int carry = 0;
    while(pointer_a >= 0 && pointer_b >= 0){
        int val = (A[pointer_a] - 48) + (B[pointer_b] - 48) + carry;
        if(val >= 10){
            carry = 1;
            val %= 10;
        } else {
            carry = 0;
        }
        char x = val + 48;
        temp.push(x);
        result += x; // append addition to the front
        pointer_a--;
        pointer_b--;
    }

    while(pointer_a >= 0){
        int val = (A[pointer_a] - 48) + carry;
        if(val >= 10){
            carry = 1;
            val %= 10;
        } else {
            carry = 0;
        }
        char x = val + 48;
        result += x; // append addition to the front
        pointer_a--;
    }

    while(pointer_b >= 0){
        int val = (B[pointer_b] - 48) + carry;
        if(val >= 10){
            carry = 1;
            val %= 10;
        } else {
            carry = 0;
        }
        char x = val + 48;
        result += x; // append addition to the front
        pointer_b--;
    }

    if(carry == 1){
        char x = carry + 48;
        result += x; // append the 1 in front
    }

    reverse(result.begin(), result.end());
    cout << result;
}