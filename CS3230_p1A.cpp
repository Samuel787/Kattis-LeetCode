#include<bits/stdc++.h>
using namespace std;

int maximum = 0;
vector<bool> sacred_heights;
vector<int> dp_heights;
int height_limit;

void helper(int curr_height, int r, int max){
    if(curr_height > height_limit){
        return; // we do not explore this path
    }
    if(sacred_heights[curr_height]){
        max += 1;
    }
    if(dp_heights[curr_height] > max){
        //we don't want this path
        return;
    } else {
        // this is the prominent path, branch from here
        dp_heights[curr_height] = max;
        if(max > maximum){
            maximum = max;
        }
        helper(curr_height + r, r, max);
        helper(curr_height + r + 1, r+ 1, max);
        if(r > 1){
            helper(curr_height + r - 1, r-1, max);
        }
    }
}

int main(){
    int r_orig;
    cin >> r_orig;
    cin >> height_limit;
    string data;
    cin >> data;
    
    for(int i = 0; i < data.size(); i++){
        if(data[i] == 's'){
            sacred_heights.push_back(true);
        } else {
            sacred_heights.push_back(false);
        }
    }

    for(int i = 0; i <= height_limit; i++){
        dp_heights.push_back(-1);
    }

    helper(0, r_orig, 0);
    cout << maximum << endl;
}