#include <bits/stdc++.h>
using namespace std;

double calcHarmonic(int n){
    double start = 0.0;
    
    for(int i = 1; i <= n; i++){
        start += 1.0/i;
        //cout << start << endl;
    }
    return start;
}

double expectedCircles(int n){
    int counter = 2;
    double result = 1;
    while(counter <= n){
        result = result + 1.0/(2.0*counter - 1);
        cout << result << endl;
        counter++;
    }
    return result;
}
int main(){
    // cout << "meow" << endl;
    // cout << calcHarmonic(200) << endl;
    // cout << calcHarmonic(100) << endl;
    // double result = calcHarmonic(200) - 0.5 * calcHarmonic(100);
    // cout << result << endl;

    cout << expectedCircles(5) << endl;
    cout << calcHarmonic(10) - 0.5*calcHarmonic(5) << endl;
}