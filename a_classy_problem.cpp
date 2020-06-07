#include <bits/stdc++.h>
using namespace std;

struct Pack{
    string name;
    string class;
};

vector<string> split_by_space(string input){
    vector<string> result;
    string temp;
    for(int i = 0; i < input.size(); i++){
        if(input[i] != ' ')
            temp += input[i]
        else{
            result.push_back(temp);
            temp = "";
        }
    }
    return result;
}

int main(){
    int NUM;
    cin >> NUM;
    while(NUM--){
        int n;
        cin >> n;
        vector<Pack> packs;
        for(int i =0; i < n; i++){
            cin.ignore();
            string line = getline();
            vector<string> result = split_by_space(line);
            Pack pack = new Pack();
            pack.name = result[0];
            pack.class = result[1];
            packs.push_back(pack);
        }

        for(int i =0; i < packs.size(); i++){
            cout << pack.name << " pack.class" << endl;
        }
    }
} 