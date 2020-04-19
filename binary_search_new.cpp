#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<int> data){
    for(int i = 0; i < data.size(); i++){
        cout << data.at(i) << ",";
    }
    cout << endl;
}

int main(){

    srand(time(nullptr));
    int rand_size = (rand() % 25) + 1;
    vector<int> data;
    for(int i = 0; i < rand_size; i++){
        data.push_back(rand());
    }

    int find = data.at(rand() % data.size());
    print_vector(data);
    cout << "i wanna find " << find << endl;
    sort(data.begin(), data.end());
    
    /**
     * Binary search implementation to find the number
    */
    int index = 0;
    for(int i = data.size()/2; i >= 1; i /= 2){
        while(index + i < data.size() && data.at(i + index) <= find){
            index += i;
        }
    }
    cout << data.at(index) << "\n";

}