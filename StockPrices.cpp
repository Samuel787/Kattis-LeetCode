#include <bits/stdc++.h>
using namespace std;

vector<string> split_to_words(string input){
    int size = input.size();
    vector<string> result;
    string temp = "";
    for(int i = 0; i < size; i++){
        if(input[i] != ' '){
            temp += input[i];
        } else {
            result.push_back(temp);
            temp = "";
        }
    }
    return result;
}

int main(){
    int T;
    cin >> T;
    while(T--){
        int n;
        cin >> n;
        cin >> ws;
        string sp = "-";
        string a = "-";
        string b = "-";
        priority_queue<int> buy;
        priority_queue<int, vector<int>, greater<int>> sell;
        for(int i = 0; i < n; i++){
            string input;
            getline(cin, input);
            input += " ";
            vector<string> data = split_to_words(input);
            int num = stoi(data[1]);
            int amount = stoi(data[4]);
            if(data[0] == "buy"){
                for(int i =0; i < num; i++){
                    buy.push(amount);
                }
            } else {
                for(int i = 0; i < num; i++){
                    sell.push(amount);
                }
            }

            while(!buy.empty() && !sell.empty() && buy.top() >= sell.top()){
                sp = to_string(sell.top());
                buy.pop();
                sell.pop();
            }

            if(buy.empty()){
                b = "-";
            } else {
                b = to_string(buy.top());
            }

            if(sell.empty()){
                a = "-";
            } else{
                a = to_string(sell.top());
            }
            cout << a << " " << b << " " << sp << endl;
        }
    }
}