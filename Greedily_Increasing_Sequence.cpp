#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    vector<int> numbers;
    int n;
    cin >> n;
    int temp;

    for(int i = 0; i < n; i++){
        cin >> temp;
        numbers.push_back(temp);
    }
    
    vector<int> new_numbers;
    new_numbers.push_back(numbers[0]);
    for(int i = 1; i < n; i++){
        if(numbers[i] > new_numbers[new_numbers.size() - 1]){
            new_numbers.push_back(numbers[i]);
        }
    }

    cout << new_numbers.size() << endl;
    
    for(int i : new_numbers){
        cout << i << " ";
    }
    
}