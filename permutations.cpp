#include <bits/stdc++.h>
using namespace std;

void permutate(string input, int l, int r){
    //base case
    if(l == r){
        cout << input << endl;
    } else {
        for(int i = l; i <= r; i++){
            swap(input[l], input[i]); //fixing the first index of the substring
            permutate(input, l+1, r);
            swap(input[l], input[i]);
        }
    }
}

int main(){
    string input;
    cin >> input;
    int length = input.size();
    permutate(input, 0, length -1);
}




// void permutate(string input, int l, int r){
//     if(l == r){
//         cout << input << endl;
//     } else {
//         permutate(input, l+1, r);
//         swap(input[l], input[l+1]);
//         permutate(input, l+1, r);
//         swap(input[l], input[l+1]);
//     }
// }

// int main(){
//     string input;
//     cin >> input;
//     int length = input.size();
//     for(int i = 0; i < length; i++){
//         swap(input[0], input[i]);
//         permutate(input, 0, length - 1);
//     }
// }