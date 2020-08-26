#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<int> data){
    for(int x: data){
        cout << x << " ";
    }
    cout << endl;
}

vector<int> helper(int N, int K, int num){
    vector<int> result;
    if(N == 0){
        result.push_back(num);
        return result; 
    }

    int prev_digit = num %= 10;
    int new_num = num * 10;
    if(prev_digit + K < 10){
        vector<int> temp = helper(N-1, K, new_num + (K + prev_digit));
        for(int x : temp){
            result.push_back(x);
        }
    }
    if(prev_digit - K >= 0){
        vector<int> temp = helper(N-1, K, new_num + (prev_digit - K));
        for(int x : temp){
            result.push_back(x);
        }
    }
    return result;
}

/**
 * main driver code for first digit
*/
vector<int> numsSameConsecDiff(int N, int K){
    vector<int> result;
    if(N == 0){
        return result;
    }
    if(N == 1){
        for(int i = 0; i < 10; i++){
            result.push_back(i);
        }
        return result;
    }
    for(int i = 1; i < 10; i++){
        vector<int> temp = helper(N-1, K, i);
        for(int x : temp) {
            result.push_back(x);
        }
    }
    return result;
}

/**
 * Driver code
*/
int main(){
    vector<int> result = numsSameConsecDiff(2, 7);
    print_vector(result);
}