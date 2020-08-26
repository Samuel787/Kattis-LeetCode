#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<int> data){
    for(int i = 0; i < data.size(); i++){
        cout << data[i] << " ";
    }
    cout << endl;
}

int countInversions(vector<int>& arr, int l, int r){
    int left = l;
    int mid = (l + r) / 2;
    int right = mid + 1;
    int inversions = 0;
    while(left <= mid){
        while(right <= r && arr[left] > arr[right]){
            right++;
        }
        inversions += right -  mid - 1;
        left++;
    }
    return inversions;
}

int merge(vector<int> &arr, int left, int mid, int right){
    
    int l = left;
    int r = mid + 1;
    int inversions = countInversions(arr, left, right);
    vector<int> temp;
    while(l <= mid && r <= right){
        if(arr[l] < arr[r]){
            temp.push_back(arr[l]);
            l++;
        } else {
            temp.push_back(arr[r]);
            r++;
        }
    }
    while(l <= mid){
        temp.push_back(arr[l]);
        l++;
    }
    while(r <= right){
        temp.push_back(arr[r]);
        r++;
    }
    int index = 0;
    for(int i = left; i <= right; i++){
        arr[i] = temp[index];
        index++;
    }
    return inversions;
}

int mergeSort(vector<int> &arr, int left, int right){
    if(right - left < 1){
        return 0;
    }
    int inversions = 0;
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    // count the inversions during the merge phase
    inversions += merge(arr, left, mid, right);
    return inversions;
}

int main(){
    // vector<int> test{4,3,2,1,0};
    // mergeSort(test, 0, test.size() - 1);

    //vector<int> test_inversions{1, 2, 3, 1, 2, 3};
    vector<int> test_inversions{1, 2, 3, 1, 2, 3};
    cout << countInversions(test_inversions, 0, test_inversions.size() - 1) << endl;
    cout << mergeSort(test_inversions, 0, test_inversions.size() - 1) << endl;
    //print_vector(test);
}