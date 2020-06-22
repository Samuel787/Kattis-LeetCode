#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

bool check_triangle(ll a, ll b, ll c){
    if(a + b <= c){
        return false;
    } else if (b + c <= a){
        return false;
    } else if (c + a <= b){
        return false;
    }
    return true;
}

int main(){
    int N;
    cin >> N;
    vector<ll> sticks;
    for(int i = 0; i < N; i++){
        ll stick;
        cin >> stick;
        sticks.push_back(stick);
    }
    //sort the sticks in ascending order
    sort(sticks.begin(), sticks.end());

    //use sliding window method from the back
    bool is_possible = false;
    for(int i = N-1; i > 1; i--){
        if(check_triangle(sticks[i], sticks[i-1], sticks[i-2])){
            is_possible = true;
            break;
        }
    }

    if(is_possible){
        cout << "possible" << endl;
    } else {
        cout << "impossible" << endl;
    }
}