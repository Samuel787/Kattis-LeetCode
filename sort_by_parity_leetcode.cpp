class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        deque<int> semi_result;
        for(int x : A){
            if(x % 2 == 0){
                semi_result.push_front(x);
            } else {
                semi_result.push_back(x);
            }
        }
        vector<int> result(semi_result.begin(), semi_result.end());
        return result;
    }
};