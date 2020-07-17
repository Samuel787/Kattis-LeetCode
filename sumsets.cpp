#include <bits/stdc++.h>
using namespace std;

bool find_3sum(vector<int> data, int high, int sum){
    for(int i = 0; i <= high; i++){
        int sub_sum = sum - data[i];
        int l = i+1;
        int h = high;
        while(l < h){
            if(data[l] + data[h] == sub_sum){
                return true;
            } else if(data[l] + data[h] < sub_sum){
                l++;
            } else {
                h++;
            }
        }
    }
    return false;
}

int main(){
    int N;
    cin >> N;
    vector<int> data;
    for(int i = 0; i < N; i++){
        int temp;
        cin >> temp;
        data.push_back(temp);
    }
    sort(data.begin(), data.end());
    if(data.size() < 4){
        cout << "no solution" << endl;
        return 0;
    }
    bool found = false;
    for(int i = data.size() - 1; i > 2 ; i--){
        //check if a sum adds up to data[i] from the remaining subset
        int sum = data[i]; //this is the d
        int high = i-1;
        if(find_3sum(data, high, sum)){
            found = true;
            cout << data[i] << endl;
            return 0;
        } 
    }
    if(!found){
        cout << "no solution" << endl;
    }
    
}
