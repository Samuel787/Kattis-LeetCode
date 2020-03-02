#include <bits/stdc++.h>
using namespace std;

int ceiling_divide(int i, int j){
    if(i % j == 0){
        return i/j;
    }
    return i/j + 1;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n;
    int k;
    cin >> k;
    int max;
    queue<int> timing;
    queue<int> servers;
    for(int i = 0; i < n; i++){
        int temp; 
        cin >> temp;
        timing.push(temp);
    }

    int running_max = 0;
    int req_time;
    while(!timing.empty()){
        req_time = timing.front();
        timing.pop();
        while(!servers.empty() && servers.front() + 1000 <= req_time){
            servers.pop(); //request has been handled, thus removed

        }
        servers.push(req_time);
        if(ceiling_divide(servers.size() , k) > running_max){
            running_max = ceiling_divide(servers.size() , k);
        }
    }

    cout << running_max << endl;

}