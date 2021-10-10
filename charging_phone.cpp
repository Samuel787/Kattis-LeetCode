#include<bits/stdc++.h>
using namespace std;

int ceiling(int x, int y) {
    int q = x / y;
    if (y * q != x) {
        return q + 1; 
    } else {
        return q;
    }
}

int chargingSmartPhone (int initCharge, int finalCharge) {
   // Write your code here
   int currCharge = initCharge;
   int minutes = 0;
    while (currCharge < finalCharge) {
        cout << "CurrCharge" << currCharge << endl;
       if (currCharge >= 0 && currCharge <= 10) {
           currCharge += 10;
           minutes += 1;
       } else if (currCharge >= 11 && currCharge <= 230) {
           int diff;
           if (finalCharge > 230) {
               diff = 231 - currCharge;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 5);
           cout << "curr charge: " << currCharge << endl;
           currCharge += mins * 5;
           minutes += mins;
       } else if (currCharge >= 231 && currCharge <= 559) {
           int diff;
           if (finalCharge > 559) {
               diff = 560 - currCharge;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 8);
           currCharge += mins * 8;
           minutes += mins;
       } else if (currCharge >= 560 && currCharge <= 1009) {
           int diff;
           if (finalCharge > 1009) {
               diff = 1010 - currCharge;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 2);
           currCharge += mins * 2;
           minutes += mins;
       } else if (currCharge >= 1010 && currCharge <= 5000) {
           int diff;
           if (finalCharge > 5000) {
               diff = 5001 - currCharge;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 7);
           currCharge += mins * 7;
           minutes += mins;
       } else if (currCharge >= 5001 && currCharge <= 10000) {
           cout << "inside branch" << endl;
           cout << "final charge" << finalCharge << endl;
           int diff;
           if (finalCharge > 10000) {
               cout << "inside condition" << endl;
               diff = 10001 - currCharge;
               cout << "diff: " << diff << endl;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 8);
           cout << "mins: " << mins << endl;
           currCharge += mins * 8;
           minutes += mins;
       } else if (currCharge >= 10001 && currCharge <= 1000000000) {
           int diff;
           if (finalCharge > 1000000000) {
               diff = 1000000001 - currCharge;
           } else {
               diff = finalCharge - currCharge;
           }
           int mins = ceiling(diff, 3);
           currCharge += mins * 3;
           minutes += mins;
       } else {
           return minutes;
       }
    }
    return minutes;
}


int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int t_i=0; t_i<T; t_i++)
    {
        int initCharge;
        cin >> initCharge;
        int finalCharge;
        cin >> finalCharge;

        int out_;
        out_ = chargingSmartPhone(initCharge, finalCharge);
        cout << out_;
        cout << "\n";
    }
}