#include <bits/stdc++.h>
using namespace std;

int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if(intervals.size() == 0) return 0;
    sort(intervals.begin(), intervals.end());

    // print the data
    for(int i = 0; i < intervals.size(); i++){
        cout << "(" << intervals[i][0] << "-" << intervals[i][1] << ")  |  ";
    }
    cout << endl;

    int last_index = 0;
    int drop_count = 0;
    cout << "Current: " << intervals[last_index][0] << " " << intervals[last_index][1] << endl;
    for(int i = 1; i < intervals.size(); i++){
        if(intervals[i][0] >= intervals[last_index][1]){
            last_index = i; // no overlap
        } else {
            //same start time
            // there is an overlap and hence, i need to drop one. I'll drop the one that ends later
            if(intervals[i][1] <= intervals[last_index][1]){
                //cout << "Current: " << intervals[last_index][0] << " " << intervals[last_index][1] << endl;
                last_index = i; 
                drop_count++; // we drop the last_index cos new one ends faster
            } else {
                
                drop_count++;
            }
        }
        cout << "Current: " << intervals[last_index][0] << " " << intervals[last_index][1] << endl;
    }
    return drop_count;
}

int main(){
    vector<vector<int>> intervals{{1, 100}, {11, 22}, {1, 11}, {2, 12}};
    int result = eraseOverlapIntervals(intervals);
    cout << result << endl;
}