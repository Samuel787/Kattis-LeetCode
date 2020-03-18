#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    bool increasing = true;
    bool decreasing = true;
    string temp;
    string prev;
    cin >> prev;
    for(int i = 1; i < n; i++){
        cin >> temp;
        if(temp > prev){
            decreasing = false;
        } else if (temp < prev){
            increasing = false;
        } 
        prev = temp;
    }
    if(increasing && !decreasing){
        cout << "INCREASING" << endl;
    } else if (decreasing && !increasing){
        cout << "DECREASING" << endl;
    } else {
        cout << "NEITHER" << endl;
    }
}