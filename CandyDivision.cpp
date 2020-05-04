#include <bits/stdc++.h>
using namespace std;

#define ll long long
int main(){
    ll N;
    cin >> N;
    vector<ll> sfactors;
    set<ll> result;
    for(ll i = 1; i <= sqrt(N); i++){
        if(N % i == 0){
            sfactors.push_back(i);
            result.insert(i-1);
        }
    }
    ll s = sfactors.size();
    for(ll i = 0; i < s; i++){
        result.insert(N/sfactors[i] - 1);
    }

    for(auto x : result){
        cout << x << " ";
    }
}