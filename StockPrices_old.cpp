#include <bits/stdc++.h>
using namespace std;

struct Pack{
    int price, amount;
};

struct minimum{
    bool operator()(const Pack &a, const Pack &b){
        return a.price > b.price;
    }
};

struct maximum{
    bool operator()(const Pack &a, const Pack &b){
        return a.price < b.price;
    }
};

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
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int T;
    cin >> T;
    while(T > 0){
        //int a, b, c;
        int n;
        cin >> n;
        if(n == 0){
            T--;
            continue;
        }
        //getchar();
        cin >> ws;
        string input;
        //getline(cin, input);
        input = "";
        priority_queue<Pack, vector<Pack>, maximum> buy;
        priority_queue<Pack, vector<Pack>, minimum> sell;
        string stock_price = "-";
        string b = "-";
        string s = "-";
        for(int i = 0; i < n; i++){
            getline(cin, input);
            input += " ";
            
            vector<string> data = split_to_words(input);
            Pack pack = Pack();
            pack.amount = stoi(data[1]);
            pack.price = stoi(data[4]);
            
            if(data[0] == "buy"){
                buy.push(pack);
            } else{
                sell.push(pack);
            }
            
            
            while(!sell.empty() && !buy.empty() &&buy.top().amount > 0){
                if(buy.top().price >= sell.top().price){
                    //person can buy
                    Pack new_pack = Pack();
                    if(buy.top().amount < sell.top().amount){
                        new_pack.amount = sell.top().amount - buy.top().amount;
                        new_pack.price = sell.top().price;
                        sell.pop();
                        sell.push(new_pack);
                        stock_price = to_string(sell.top().price);
                        buy.pop();
                    } else if(buy.top().amount == sell.top().amount){
                        stock_price = to_string(sell.top().price);
                        buy.pop();
                        sell.pop();
                    } else{
                        new_pack.amount = buy.top().amount - sell.top().amount;
                        new_pack.price = sell.top().price;
                        stock_price = to_string(sell.top().price);
                        buy.pop();
                        buy.push(new_pack);
                        sell.pop();
                    }
                } else {
                    break;
                }
            }
            if(!buy.empty()){
                b = to_string(buy.top().price);
            } else {
                b = "-";
            }
            if(!sell.empty()){
                s = to_string(sell.top().price);
            } else {
                s = "-";
            }
            cout << s << " " << b << " " << stock_price << endl; 
        }
        T--;
    }
}
