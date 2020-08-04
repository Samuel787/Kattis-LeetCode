class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int first_pos = -1;
        for(int i = 0; i < A.size(); i++){
            if(A[i] >= 0){
                first_pos = i; 
                break;
            }
        }
        
        vector<int> result;
        if(first_pos == -1){
            //all the values are negative
            for(int i = A.size()-1; i >= 0; i--){
                result.push_back(pow(A[i], 2));
            }
            return result;
        }
        
        int left = first_pos - 1;
        int right = first_pos;
        //result.push_back(pow(A[first_pos], 2));
        while(left >= 0 && right <= A.size() - 1){
            if(-A[left] > A[right]){
                cout << A[right] << endl;
                result.push_back(pow(A[right], 2));
                right++;
            } else{
                cout << A[left] << endl;
                result.push_back(pow(A[left], 2));
                left--;
            }
        }
        
        while(left >= 0){
            result.push_back(pow(A[left], 2));
            left--;
        }
        while(right < A.size()){
            result.push_back(pow(A[right], 2));
            right++;
        }
        return result;
    }
};