class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool carry = true;
        for(int i = digits.size() - 1; i >= 0 ; i--){
            if(carry){
                digits[i] += 1;
                if(digits[i] > 9){
                    carry = true;
                    digits[i] %= 10;
                } else {
                    carry = false;
                }
            }
        }
        if(carry){
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
