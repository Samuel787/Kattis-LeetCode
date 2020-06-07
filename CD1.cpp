#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int N, M;
    while(cin >> N >> M){
        if (N == 0 && M == 0){
            break;
        }
        unordered_set<int> data;
        int temp;
        for(int i = 0; i < N; i++){
            cin >> temp;
            data.insert(temp);
        }   
        int counter = 0;
        for(int i = 0; i < M; i++){
            cin >> temp;
            if(data.find(temp) != data.end()){
                counter++;
            }
        }
        cout <<counter<< endl;
    }
}

    // int N, M;
    // while(cin >> N >> M){
    //     if(N == 0 && M == 0){
    //         break;
    //     }
    //     vector<bool>  data(INT32_MAX, false);
        
    //     int temp;
    //     for(int i = 0; i < N; i ++){
    //         cin >> temp;
    //         data[temp] = true;
    //     }

    //     int common = 0;
    //     for(int i = 0; i < M; i ++){
    //         cin >> temp;
    //         if (data[temp] == true){
    //             common++;
    //         }
    //     }
    //     cout << N + M - common * 2 << endl;
    // }