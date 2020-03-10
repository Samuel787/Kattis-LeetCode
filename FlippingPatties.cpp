#include <bits/stdc++.h>
using namespace std;

int ceil_divide(int i){
    if(i % 2 == 0){
        return i/2;
    } else {
        return (i+1)/2;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    vector<int> hands(43201, 0);
    int num;
    cin >> num;
    int d;
    int t;
    for(int i = 0; i < num; i++){
        cin >> d;
        cin >> t;
        hands[t - 2*d]++; //place patty on grill
        hands[t - d]++; //flip the patty on the grill
        hands[t]++; // remove patty from grill to serve customer
    }

    int max = hands[0];
    //calculate the running max inside the hands
    for(int i = 1; i < 43201; i++){
        if(hands[i] > max)
            max = hands[i];
    }
    
    cout << ceil_divide(max) << endl;
}