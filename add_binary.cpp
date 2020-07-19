#include <bits/stdc++.h>
using namespace std;

string addBinary(string a, string b){
    //step 1, make both the strings the same size by appending 0s
    if(a.length() < b.length()){
        int diff = b.length() - a.length();
        string temp = "";
        for(int i = 0; i < diff; i++){
            temp += "0";
        }
        a = temp + a;
    } else if(a.length() > b.length()){
        int diff = a.length() - b.length();
        string temp = "";
        for(int i = 0; i < diff; i++){
            temp += "0";
        }
        b = temp + b;
    }

    stack<char> result;
    int aL = a.length() - 1;
    int bL = b.length() - 1;
    char carry = '0';
    while(aL != -1 && bL != -1){
        if(a[aL] == '1' && b[bL] == '1' && carry == '0'){
            carry = '1';
            result.push('0');
            aL--;
            bL--;
        } else if(a[aL] == '1' && b[bL] == '1' && carry == '1'){
            carry = '1';
            result.push('1');
            aL--;
            bL--;
        } else if(((a[aL] == '0' && b[bL] == '1') || (a[aL] == '1' && b[bL] == '0')) && carry == '0'){
            carry = '0';
            result.push('1');
            aL--;
            bL--;
        } else if(((a[aL] == '0' && b[bL] == '1') || (a[aL] == '1' && b[bL] == '0')) && carry == '1'){
            carry = '1';
            result.push('0');
            aL--;
            bL--;
        } else if(a[aL] == '0' && b[bL] == '0' && carry == '0'){
            carry = '0';
            result.push('0');
            aL--;
            bL--;
        } else if(a[aL] == '0' && b[bL] == '0' && carry == '1'){
            carry = '0';
            result.push('1');
            aL--;
            bL--;
        } else {
            cout << "I did not take note of this case where a=" << a[aL] << "and b=" << b[bL] << "and carry " << carry << endl;
        }
    }

    //dump the carry onto the stack
    if(carry == '1'){
        result.push(carry);
    }
    //parse stack into a string and return it
    string res = "";
    while(!result.empty()){
        res += result.top();
        result.pop();
    }
    return res;
}

/*
    Driver code
*/
int main(){
    string a = "1010";
    string b = "1011";
    cout << addBinary(a, b) << endl;
}