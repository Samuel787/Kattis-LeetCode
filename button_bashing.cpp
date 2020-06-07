#include <bits/stdc++.h>
using namespace std;

void print_set(set<pair<int, int>> mSet){
    for(set<pair<int, int>> :: iterator x = mSet.begin(); x != mSet.end(); x++){
        cout << "{" << (*x).first << "," << (*x).second <<"}" << " ";
    }
    cout << endl;
}
int main(){
    int num;
    cin >> num;
    while(num--){
        int num_btns;
        cin >> num_btns;
        int timing;
        cin >> timing;
        vector<int> btns;
        for(int i = 0; i < num_btns; i++){
             int btn;
             cin >> btn;
             btns.push_back(btn);
        }
        if(timing == 0){
            cout << 0 << " " << 0 << endl;
            continue;
        }
        vector<int> visited_timing_vect(3601, 1000000000);
        queue<pair<int, int>> frontier;
        pair<int, int> start= make_pair(0, 0); //first element of pair is STEPS and second element is the TIMING
        frontier.push(start);
        bool isFound = false;
        while(!frontier.empty()){
            pair<int, int> curr = frontier.front();
            frontier.pop();
            visited_timing_vect[curr.second] = curr.first;
            for(int i = 0; i < btns.size(); i++){
                int new_steps = (curr.first) + 1;
                int new_timing = (curr.second) + btns[i];
                if(new_timing > 3600) new_timing = 3600;
                if(new_timing < 0) new_timing = 0;
                if(new_timing == timing){
                    cout << new_steps << " " << 0 << endl; 
                    isFound = true;
                    break;
                } 
                // if(visited_timing_vect[new_timing] == -1){
                //     pair<int, int> new_pair = make_pair(new_steps, new_timing);
                //     frontier.push(new_pair);
                //     visited_timing_vect[new_timing] = new_steps;
                // }
                if(new_steps < visited_timing_vect[new_timing]){
                    pair<int, int> new_pair = make_pair(new_steps, new_timing);
                    frontier.push(new_pair);
                    visited_timing_vect[new_timing] = new_steps;
                }
            }
            if(isFound) break;
        }
        if(!isFound){
            for(int i = timing+1; i < 3601; i++){
                if(visited_timing_vect[i] != 1000000000){
                    cout << visited_timing_vect[i] << " " << i - timing << endl;
                    break;
                }
            }  
        }
 
    }
}


















// #include <bits/stdc++.h>
// using namespace std;

// void print_set(set<pair<int, int>> mSet){
//     for(set<pair<int, int>> :: iterator x = mSet.begin(); x != mSet.end(); x++){
//         cout << "{" << (*x).first << "," << (*x).second <<"}" << " ";
//     }
//     cout << endl;
// }
// int main(){
//     int num;
//     cin >> num;
//     while(num--){
//         int num_btns;
//         cin >> num_btns;
//         int timing;
//         cin >> timing;
//         vector<int> btns;
//         for(int i = 0; i < num_btns; i++){
//              int btn;
//              cin >> btn;
//              btns.push_back(btn);
//         }
//         //each pair will contain num steps and the timing
//         set<pair<int, int>> visited; //automatically a sorted set
//         unordered_set<int> visited_timing;
//         queue<pair<int, int>> frontier;
//         pair<int, int> start= make_pair(0, 0);
//         frontier.push(start);
//         bool isFound = false;
//         while(!frontier.empty()){
//             pair<int, int> curr = frontier.front();
//             frontier.pop();
//             //cout << "generating" << endl;
//             visited.insert(curr);
//             visited_timing.insert(curr.second);
//             //generate all the neighbors from curr:
//             for(int i = 0; i < btns.size(); i++){
//                 int new_steps = (curr.first) + 1;
//                 int new_timing = (curr.second) + btns[i];
//                 if(new_timing > 3600) new_timing = 3600;
//                 if(new_timing < 0) new_timing = 0;
//                 if(new_timing == timing){
//                     cout << new_steps << " " << 0 << endl; 
//                     isFound = true;
//                     break;
//                 } 
//                 if(visited_timing.size() == 3601){
//                     isFound = true;
//                     break;
//                 }
//                 if(visited_timing.find(new_timing) == visited_timing.end()){
//                     pair<int, int> new_pair = make_pair(new_steps, new_timing);
//                     frontier.push(new_pair);
//                 }
//             }
//             if(isFound) break;
//         }
//         if(!isFound){
//             for(set<pair<int, int>>::iterator x = visited.begin(); x != visited.end(); x++){
//                 if((*x).second >= timing){
//                     cout << (*x).first << " " << ((*x).second - timing) << endl;
//                     break;
//                 }
//             }    
//         }
 
//     }
// }
