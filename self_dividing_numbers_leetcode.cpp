class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> result;
        for(int i = left; i <= right; i++){
            if(is_self_dividing(i)){
                result.push_back(i);
            }
        }
        return result;
    }
    
    bool is_self_dividing(int k){
        int copy = k;
        while(k > 0){
            int num = k%10;
            if(num == 0){
                return false;
            }
            if(copy % num == 0){
                k /= 10;
                continue;
            } else {
                return false;
            }
        }
        return true;
    }
};