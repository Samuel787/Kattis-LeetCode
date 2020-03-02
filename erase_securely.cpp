#include <bits/stdc++.h>
using namespace std;

void check_result(string initial, string result){
    if(initial == result){
        cout << "Deletion succeeded" << endl;
    } else {
        cout << "Deletion failed" << endl;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n; //number of times to sweep

    string initial, result;
    cin >> initial;
    cin >> result;
    
    int length = initial.size();
    string j, k;
    if(n %2 == 0){
        check_result(initial, result);
    } else {
        //change the initial
        for(int i = 0; i < length; i++){
            if(initial[i] == '1'){
                initial[i] = '0';
            } else {
                initial[i] = '1';
            }
        }
        check_result(initial, result);
    }


    // string meow = "meow";
    // cout << meow[1] << endl;
}