#include <bits/stdc++.h>
using namespace std;

/**
 * @param training is a 2d array. Each array inside training has this
 * composition: feature 1: arr[0], feature 2: arr[1], label: arr[2]
 * @param test is a 1d array. This array has this composition:
 * feature 1: arr[0], feature 2: arr[1]
 * @return result 
*/
int calculateKNN(vector<vector<double>> training, vector<double> test){
    int count[2];
    count[0] = 0;
    count[1] = 0;
    priority_queue<pair<double, int>> pq; // to store euclidean dist in asc order

    int K = 5; // set K here. Since the function can't take this as argument
    if(K < 1 || K > training.size()) return -1; //invalid value for K!

    for(vector<double> train : training){
        double euclidean_dist = pow((train[0] - test[0]), 2) - pow((train[1] - test[1]), 2);
        //cout << "Euclidean dist" << euclidean_dist << endl;
        pq.push(make_pair(euclidean_dist, train[2]));
    }

    for(int i = 0; i < K; i++){
        count[pq.top().second]++;
        //cout << "incrementing: " << pq.top().second << endl;
        pq.pop();
    }

    //cout << "Count of 0: " << count[0] << endl;
    //cout << "Count of 1: " << count[1] << endl;
    if(count[0] > count[1]){
        return 0;
    } else if(count[0] < count[1]){
        return 1; 
    } else {
        srand(time(0));
        if(rand()/(double)RAND_MAX >= 0.5){
            return 1;
        } else {
            return 0;
        }
    }
}

/**
 *  Driver code
*/
int main(){
    vector<vector<double>> training_data{{1,2,1},{1,3,0},{1,4,1},{2,3,0},{1,2,1},{1,3,0},{1,4,1},{2,3,0},{1,2,1},{1,3,0},{1,41,1},{2,32,0},{1,212,1},{1,343,0},{1,4,1},{2,3,0},{100,2,1},{1,30,0},{1,400,1},{2,3,0},{1.8,2,1},{1,33,0},{112,4,1},{11.5,3,0}};

    vector<double> test_point{2, 3};
    cout << calculateKNN(training_data, test_point) << endl;
}