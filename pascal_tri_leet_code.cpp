#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> generate(int numRows) {
        vector<vector<int>> tri;
        for(int i = 0; i < numRows; i++){
            vector<int> row;
            if(i == 0){
                row.push_back(1);
                tri.push_back(row);
            } else {
                for(int j = 0; j < i; j++){
                    if(j == 0 || j == i-1){
                        row.push_back(1);
                    } else {
                        row.push_back(tri[i-1][j-1] + tri[i-1][j]);
                    }
                }
                tri.push_back(row);
            }
        }
        return tri;
}

void print_soln(vector<vector<int>> lol){
    for(int i = 0; i < lol.size(); i++){
        for(int j = 0; j < lol[i].size(); j++){
            cout << lol[i][j] << " "; 
        }
        cout << endl;
    }
}

int main(){
    int n;
    cin >> n;
    print_soln(generate(n));
}