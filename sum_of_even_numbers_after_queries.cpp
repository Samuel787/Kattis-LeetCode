class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        int initial_sum = 0;
        vector<int> result;
        for(int i = 0; i < A.size(); i++){
            if(A[i] % 2 == 0){
                initial_sum += A[i];
            }
        }
        for(int i = 0; i < queries.size(); i++){
            int val = queries[i][0];
            int index = queries[i][1];
            int initial_val = A[index];
            A[index] += val;
            if(is_even(initial_val) && is_even(val)){
                initial_sum += val;
            } else if (is_even(initial_val) && !is_even(val)){
                initial_sum -= initial_val;
            } else if (!is_even(initial_val) && is_even(val)){
                cout << "third case" << endl;
            } else {
                initial_sum += A[index];
            }
            result.push_back(initial_sum);
        }
        return result;
    }
    
    bool is_even(int x){
        int res = x % 2;
        if(res == 0) {
            return true;
        } else {
            return false;
        }
    }
};