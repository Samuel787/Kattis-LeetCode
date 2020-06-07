#include <bits/stdc++.h>
using namespace std;

int main(){
    multimap<int, int> test;
    test.insert(pair<int, int>(1, 20));
    test.insert(pair<int, int>(1, 10));
    auto x = test.find(1);
    cout << x -> second << endl;
    //cout << test.find(1) << endl;
    cout << "---" << endl;
    multimap<int, int> :: iterator it= test.begin();
    while(it != test.end()){
        cout << it -> second << endl;
        it++;
    }
}