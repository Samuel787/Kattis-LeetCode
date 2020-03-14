#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    stack<int> cards;
    int curr;
    for(int i = 0; i < n; i++){
        cin >> curr;
        if(cards.empty()){
            cards.push(curr);
        } else {
            if((cards.top() + curr) % 2 == 0){
                cards.pop();
            } else {
                cards.push(curr);
            }
        }
    }
    cout << cards.size() << endl;
}
