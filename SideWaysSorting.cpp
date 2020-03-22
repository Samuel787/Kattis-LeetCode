#include <bits/stdc++.h>
using namespace std;

int main(){
    int r, c;
    // cin >> r >> c;
    while(cin >> r >> c){
        if(r == 0 && c == 0){
            break;
        }

        vector<string> rows;
        string temp;

        //input layer
        for(int i = 0; i < r; i++){
            cin >> temp;
            rows.push_back(temp);
        }

        //processing layer
        vector<string> processing;
        for(int i = 0; i < c; i++){
            char p_temp[r+1];
            for(int j = 0; j < r; j++){
                p_temp[j] = rows[j][i];
            }
            p_temp[r] = '\0';
            processing.push_back(p_temp);
        }

        stable_sort(processing.begin(), processing.end(), [](string a, string b){
            int length = min(a.size(), b.size());
            for(int i = 0; i < length; i++){
                if(tolower(a[i]) == tolower(b[i])){
                    continue;
                } else {
                    return tolower(a[i]) < tolower(b[i]);
                }
            }
            
            if(a.size() < b.size()){
                return true;
            } else {
                return false;
            }
        });

        // stable_sort(processing.begin(), processing.end(), [](string a, string b){
        //     int length = min(a.size(), b.size());
        //     for(int i = 0; i < length; i++){
        //         if(a[i] < 97 && b[i] < 97){
        //             //both capital
        //             if(a[i] == b[i]){
        //                 continue;
        //             } else {
        //                 return a[i] < b[i];
        //             }
        //         } else if(a[i] >= 97 && b[i] >= 97){
        //             //both small
        //             if(a[i] == b[i]){
        //                 continue;
        //             } else {
        //                 return a[i] < b[i];
        //             }
        //         } else if(a[i] >= 97 && b[i] < 97){
        //             if(a[i] ==  (b[i] + 32)){
        //                 return false;
        //             } else if (a[i] > (b[i] + 32)){
        //                 return false;
        //             } else {
        //                 return true;
        //             }
        //         } else {
        //             //a[i] is capital and b[i] is small
        //             if(a[i] == (b[i] - 32)){
        //                 return true;
        //             } else if(a[i] > (b[i] - 32)){
        //                 return false;
        //             } else {
        //                 return true;
        //             }
        //         }
        //     }
        //     //looped through the smallest string already and so far they equal
        //     if(a.size() <= b.size()){
        //         return true;
        //     } else {
        //         return false;
        //     }
        // });
    
        //output layer
        vector<string> output;
        for(int i = 0; i < r; i++){
            char o_temp[c+1];
            for(int j = 0; j < c; j++){
                o_temp[j] = processing[j][i];
            }
            o_temp[c] = '\0';
            output.push_back(o_temp);
        }

        for(int i = 0; i < output.size(); i++){
            cout << output[i] << endl;
        }
    }
}