#include <bits/stdc++.h>
using namespace std;

vector<string> helper(string characters, int length){
    vector<string> results;
    if(length <= 0 || length > characters.size()){
        return results;
    }
    if(length == 1){
        for(int i = 0; i < characters.size(); i++){
            string temp = characters[i] + "";
            cout << "base case temp: " << temp << endl;
            results.push_back(temp);
            
        }
        return results;
    }
    
    vector<string> sub_results;
    sub_results = helper(characters.substr(1, characters.size() - 1), length - 1);
    string curr = characters[0] + "";
    cout << "curr is: " << curr << endl;
    for(int i = 0; i < sub_results.size(); i++){
        string temp = curr + sub_results[i];
        cout << "sub_result: " << temp << endl;
        results.push_back(temp);
    }

    return results;
}

int main(){
    string test = "abcde";
    vector<string> result = helper(test, 2);
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    cout << endl;
}
