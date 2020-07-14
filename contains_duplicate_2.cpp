#include <bits/stdc++.h>
using namespace std;


int main(){
    vector<int> nums{1, 2, 3, 1};
    int k = 3;
    bool found = false;
    vector<pair<int,int>> n;
    for(int i = 0; i < nums.size(); i++){
        n.push_back(make_pair(nums[i], i));
    }
    sort(n.begin(), n.end());
    for(int i = 1; i < n.size(); i++){
        if(n[i].first == n[i-1].first){
            if(n[i].second - n[i-1].second <= k){
                found = true;
                cout << "true" << endl;
            }
        }
    }
    if(!found){
        cout << "false" << endl;
    }
}