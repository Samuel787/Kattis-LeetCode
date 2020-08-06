#include <bits/stdc++.h>
using namespace std;


/**
 * The solution that works in O(n) time. :O
 */
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;
        while(left < right){
            if(height[left] < height[right]){
                int area = height[left] * (right - left);
                max_area = max(area, max_area);
                left++;
            } else {
                int area = height[right] * (right - left);
                max_area = max(area, max_area);
                right--;
            }
        }
        return max_area;
    }
};

/**
 * This code TLE-ed cos O(n2)
*/
int maxArea(vector<int>& height) {
    int max;
    int max2;
    int width1;
    int width2;

    vector<int> areas;
    for(int i = 0; i < height.size(); i++){
        int leftIndex = i;
        int rightIndex = i;
        
        int leftMax = height[i];
        int rightMax = height[i];
        
        //search left
        for(int j =i - 1; j >= 0; j--){
            if(height[j] >= height[i]){
                leftMax = height[j];
                leftIndex = j;
            }
        }
        
        //search right
        for(int j = i + 1; j < height.size(); j++){
            if(height[j] >= height[i]){
                rightMax = height[j];
                rightIndex = j;
            }
        }
        
        int leftHeight = min(height[i], height[leftIndex]);
        int leftArea = (i - leftIndex) * (leftHeight);
        if(leftArea < 0) leftArea *= -1;
        
        
        int rightHeight = min(height[i], height[rightIndex]);
        int rightArea = (rightIndex - i) * (rightHeight);
        if(rightArea < 0) rightArea *= -1;

        cout << "leftArea: " << leftArea << endl;
        cout << "right Area: " << rightArea << endl;
        cout << "right Height: " << rightHeight << endl;
        cout << "right width " << rightIndex - i << endl;
        cout << "right index " << rightIndex << endl;
        cout << "i value: " << i << endl;
        
        if(leftArea > rightArea){
            cout << leftArea << endl;
            areas.push_back(leftArea);
        } else {
            cout << leftArea << endl;
            areas.push_back(rightArea);
        }
    }
    
    int maxArea = 0;
    for(int i = 0; i < areas.size(); i++){
        if(areas[i] > maxArea)
            maxArea= areas[i];
    }
    return maxArea;
}

/**
 * Driver code
*/
int main(){
    //vector<int> heights{1, 8, 6, 2, 5, 4, 8, 3, 7};
    vector<int> heights{1, 2,1};
    cout << maxArea(heights) << endl;
}