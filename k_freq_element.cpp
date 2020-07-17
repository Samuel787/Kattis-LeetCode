#include <bits/stdc++.h>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    vector<int> result;
    map<int, int> count;
    for(int i = 0; i < nums.size(); i++){
        count[nums[i]]++;
    }
    vector<pair<int, int>> to_sort;
    for(map<int, int>::iterator itr = count.begin(); itr != count.end(); itr++){
        to_sort.push_back(make_pair(itr->second, itr->first));
    }
    sort(to_sort.begin(), to_sort.end());
    cout << "hello" << to_sort.size() << endl;
    cout << "i: " << to_sort.size() - 1 << endl;
    cout << "limit: " << to_sort.size() - k << endl;
    for(int i = to_sort.size()-1; i >= to_sort.size()-k; i--){
        cout << "hello " << i << endl;
        cout << to_sort[i].second << endl;
        result.push_back(to_sort[i].second);
        if(i==0) break;
    }
    return result;
}

/*
    Driver code
*/
int main(){
    vector<int> input{1, 2};
    int k = 2;
    vector<int> result = topKFrequent(input, k);
    cout << "=====result=====" << endl;
    for(int i = 0; i < result.size(); i++){
        cout << result[i] << " ";
    }
    cout << endl;
}