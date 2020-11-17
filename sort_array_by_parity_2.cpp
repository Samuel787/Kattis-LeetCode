class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int even_pointer = 0;
        int odd_pointer = 1;
        if(A.size() < 2){
            return A;
        }
        while(odd_pointer < A.size() && even_pointer < A.size()){
            if(A[even_pointer] % 2 != 0){
                while(odd_pointer < A.size() && A[odd_pointer] % 2 != 0){
                    odd_pointer += 2;
                }    
                int temp = A[even_pointer];
                A[even_pointer] = A[odd_pointer];
                A[odd_pointer] = temp;
            }
            even_pointer += 2;
        }
        return A;
    }
};