class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int low = 0;
        int high = arr.size() - 1;
        
        while (high - low + 1 > k) {
            int low_closeness = findCloseness(arr[low], x);
            int high_closeness = findCloseness(arr[high], x);
            if (low_closeness <= high_closeness) {
                high--;
            } else {
                low++;
            } 
        }
        vector<int> result;
        for (int i = low; i <= high; i++) {
            result.push_back(arr[i]);
        }
        return result;
    }
    
    int findCloseness(int x, int y) {
        return  x >= y ? x - y : y - x;
    }
};