#include <bits/stdc++.h>
using namespace std;

int sumOfThree(vector<int> arr, int k){
    sort(arr.begin(), arr.end());
    int counter = 0; // counts the unique unordered triplets

    if(arr.size() < 3){
        return counter;
    } 

    for(int i = 0; i < arr.size() - 2; i++){
        if(i == 0 || arr[i] != arr[i - 1]){
            //find two numbers that add up to the sum
            int sum = k - arr[i];
            int low = i + 1;
            int high = arr.size() - 1;
            while(low < high){
                if(arr[low] = arr[high] == sum){
                    counter++;
                    while(low < high && arr[low] == arr[low + 1]) low++;
                    while(low < high && arr[high] == arr[high - 1]) high--;
                    low++;
                    high--;
                } else if(arr[low] + arr[high] < sum){
                    low++;
                } else {
                    high--;
                }
            }
        }
    }
    return counter;
}

/*
    Driver code
*/
int main(){

}