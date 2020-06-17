#include <bits/stdc++.h>
using namespace std;

struct Pack{
    string name;
    string mClass;
    vector<int> vClass;
};

vector<string> split_by_colon(string input){
    vector<string> result;
    string temp = "";
    for(int i = 0; i < input.size(); i++){
        if(input[i] != ':'){
            temp += input[i];
            if(i == input.size() - 1){
                result.push_back(temp);
            }
        } else {
            result.push_back(temp);
            temp = "";

        }
    }
    return result;
}

vector<string> split_by_space(string input){
    vector<string> result;
    string temp;
    for(int i = 0; i < input.size(); i++){
        if(input[i] != ' '){
            temp += input[i];
            if(i == input.size() - 1){
                result.push_back(temp);
            }
        } else{
            result.push_back(temp);
            temp = "";
        }
    }
    return result;
}

vector<string> split_by_dash(string input){
    vector<string> result;
    string temp;
    for(int i = 0; i < input.size(); i++){
        if(input[i] != '-'){
            temp += input[i];
            if(i == input.size() - 1){
                result.push_back(temp);
            }
        } else {
            result.push_back(temp);
            temp = "";
        }
    }
    return result;
}

vector<int> classify_classes(vector<string> input){
    vector<int> result;
    for(int i = 0; i < input.size(); i++){
        if(input[i] == "upper"){
            result.push_back(2);
        } else if(input[i] == "middle"){
            result.push_back(1);
        } else {
            result.push_back(0);
        }
    }
    return result;
}

string print_vector(vector<int> input){
    string result = "";
    for(int i = 0; i < input.size(); i++){
        result += input[i];
    }
    return result;
}
int main(){
    int NUM;
    cin >> NUM;
    while(NUM--){
        int n;
        cin >> n;
        cin.ignore();
        vector<Pack> packs;
        for(int i =0; i < n; i++){
            string line;
            getline(cin, line);
            vector<string> result1 = split_by_colon(line);
            Pack pack = {};
            pack.name = result1[0];
            pack.mClass = split_by_space(result1[1])[1];
            pack.vClass = classify_classes(split_by_dash(pack.mClass));
            packs.push_back(pack);
        }

        sort(packs.begin(), packs.end(), [](const Pack &first, const Pack &second){
            int smaller = (first.vClass.size() > second.vClass.size()) ? second.vClass.size() : first.vClass.size();
            
            vector<int> firstClass = first.vClass;
            vector<int> secondClass = second.vClass;
            //first we have to make the size of the two vectors equal firs then only do the comparison
            if(first.vClass.size() == smaller){
                for(int i = 0; i <second.vClass.size() - smaller; i++){
                    firstClass.insert(firstClass.begin(), 1);
                }
            } else {
                for(int i = 0; i < first.vClass.size() - smaller; i++){
                    secondClass.insert(secondClass.begin(), 1);
                }
            }
            int length = secondClass.size();
            for(int i = length - 1; i >= 0; i--){
                if(firstClass[i] > secondClass[i]){
                    //cout << first.name << firstClass[i] << second.name << secondClass[i] << endl;
                    return true;
                } else if(firstClass[i] < secondClass[i]){
                    return false;
                } else {
                    continue;
                }
            }
            //up to the smaller vector, both have the same classes
            if(first.name == second.name){
                return false; // don't swap
            } 
            return first.name < second.name;
        });

        for(int i =0; i < packs.size(); i++){
            cout << packs[i].name << endl;
        }
        cout << "==============================" << endl;
        
    }
} 