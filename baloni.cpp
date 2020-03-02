#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    //reading and storing the inputs
    int N;
    cin >> N;
    vector<int> balloons;
    int temp;
    for(int i = 0; i < N; i++){
        cin >> temp;
        balloons.push_back(temp);
    }
    vector<int> arrows;
    int curr_balloon;
    
    for(int i = 0; i < N; i++){
        curr_balloon = balloons.at(i);
        int pos = -1;
        for(int j = 0; j < arrows.size(); j++){
            //find arrow to pop balloon at [i]
            if(arrows.at(j) == curr_balloon){
                pos = j;
                break;
            }
        }

        if(pos != -1){
            //found an arrow
            arrows.at(pos) -= 1;
        } else {
            //spawn a new arrow
            arrows.push_back(curr_balloon - 1);
        }
        balloons.at(i) = 0;
    }
    cout << arrows.size();
}