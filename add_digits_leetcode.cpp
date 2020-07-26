#include <bits/stdc++.h>
using namespace std;

int addDigits(int num) {

    if(num == 0){
        return 0;
    } else if (num % 9 == 0){
        return 9;
    } else {
        return num % 9;
    }

    // Naive implementation
    // if(num < 10){
    //     return num;
    // }
    // //add the digits and return the sum of the digits
    // int length = 0;
    // int num_copy = num;
    // do{
    //     length++;
    //     num_copy /= 10;
    // } while(num_copy);

    // int sum = 0;
    // while(num > 0){
    //     int digit = num / pow(10, length - 1);
    //     sum += digit;
    //     num -= digit * pow(10, length - 1);
    //     cout << "new number " << num << endl;
    //     length--;
    // }
    // return addDigits(sum);
}
    
/**
 * 
 *  Driver code
 */
int main(){
    int num = 11;
    cout << addDigits(11) << endl;
}