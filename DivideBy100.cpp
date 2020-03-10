#include <bits/stdc++.h>
using namespace std;

void trim_zeroes(char* result, int len){

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string dividend;
    string divisor;
    cin >> dividend;
    cin >> divisor;

    int power = divisor.length();
    int input_length = dividend.length();
    if(power ==  1){
        //just dividing by 1
        cout << dividend;
    } else if(power <= input_length) {
        int decimal_index = input_length - power + 1;
        char result[input_length + 2];
        for(int i = 0; i < decimal_index; i++){
            result[i] = dividend[i];
        } 
        result[decimal_index] = '.';
        for(int i = decimal_index+1; i <= input_length; i++){
            result[i] = dividend[i - 1];
        }
        result[input_length+1] = '\0'; 
        
        int index = input_length;
        //int len = input_length+2;
        while(index > 0){
            if(result[index] == '.'){
                result[index] = '\0';
                break;
            }
            if(result[index] != '0'){
                result[index + 1] = '\0';
                break;
            } 
            index--;
        }
        cout << result;
    } else {
        char result[power + 2];
        //number of leading zeroes to add
        result[0] = '0';
        result[1] = '.';
        int num = power - input_length - 1;
        for(int i = 0; i < num; i++){
            result[2 + i] = '0';
        }
        for(int j = num; j < num + input_length; j++){
            result[j + 2] = dividend[j - num];
        }
        result[power + 1] = '\0';
        //trimming last few zeroes
        int index = power + 1;
        while(index > 0){
            if(result[index] != '0'){
                result[index + 1] = '\0';
                break;
            }
            index--;
        }
        cout << result;
    }
}