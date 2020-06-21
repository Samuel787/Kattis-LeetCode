#include <bits/stdc++.h>
using namespace std;

void permutate(string input, int l, int r){
    //base case
    if(l == r){
        //fixed all the letters from start to end (reached bottom of the recursion tree)
        cout << input << endl;
    } else {

        //getting all the permutation of the string by swapping the first index with every index
        for(int i = l; i <= r; i++){
            swap(input[l], input[i]); //fixing the first index of the substring
            permutate(input, l+1, r); //permutate the letters from l + 1 to r indices
            swap(input[l], input[i]); //restore the original string
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