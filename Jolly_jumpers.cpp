#include <bits/stdc++.h>
using namespace std;

bool check_jolly(vector<bool> jolly){
    bool result = true;
    for(int i = 1; i < jolly.size(); i++){
        if(jolly.at(i) == false){
            result = false;
            break;
        }
    }
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string s;
    int n;
    while(cin >> n){
        int temp;
        //read input O(n)
        vector<int> numbers;
        for(int i = 0; i < n; i++){
            cin >> temp;
            numbers.push_back(temp);
        }

        //o(n)
        vector<bool> jolly;
        for(int i = 0; i < n; i++){
            jolly.push_back(false);
        }

        int dif = 0;
        for(int i = 1; i < n; i++){
            dif = numbers.at(i) - numbers.at(i-1);
            if(dif < 0){
                dif *= -1;
            }
            jolly[dif] = true;
        }

        if(check_jolly(jolly)){
            cout << "Jolly" << endl;
        } else {
            cout << "Not jolly" << endl;
        }
    }

}