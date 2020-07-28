#include <bits/stdc++.h>
using namespace std;

int leastInterval(vector<char>& tasks, int n) {
    vector<int> mTasks(26, 0);
    for(char t : tasks){
        mTasks[t - 65]++;
    }
    
    sort(mTasks.begin(), mTasks.end());
    
    int max_val = (mTasks[25] - 1);
    int num_idle = n * max_val; //this will contain the maximum number of occurrance

    for(int i = 0; i <= 24; i++){
        num_idle -= min(mTasks[i], max_val);
    }
    return (num_idle > 0) ? tasks.size() + num_idle: tasks.size();
}


/**
 * Main driver coder
 */
int main(){
    vector<char> tasks{'A','A','A','A','A','A','B','C','D','E','F','G'};
    int n = 2;
    cout << "F" << endl;
    cout << leastInterval(tasks, 2) << endl;
    cout << "F" << endl;
}