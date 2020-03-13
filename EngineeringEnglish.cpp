#include <bits/stdc++.h>
using namespace std;

int main(){
    string word;
    string word_copy;
    string output = "";
    unordered_set<string> data;
    while(cin >> word){
        word_copy = word;
        transform(word_copy.begin(), word_copy.end(), word_copy.begin(), ::tolower);
        if(data.find(word_copy) == data.end()){
            data.insert(word_copy);
            output += word + " ";
        } else {
            output += ". ";
        }
    }
    cout << output;
}