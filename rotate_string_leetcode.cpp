class Solution {
public:
    bool rotateString(string A, string B) {
        if(A.size() != B.size()){
            return false;
        }
        if(A.size() == 0){
            return true;
        }
        int a_pointer = 0;
        int b_pointer = 0;
        int length = A.size();
        while(b_pointer < length){
            if(A[a_pointer] == B[b_pointer]){
                //check
                int a = 0;
                int b = b_pointer;
                while(a < length){
                    if(A[a] != B[b]){
                        break;
                    }
                    a++;
                    b++;
                    b %= length;
                }
                if(a == length){
                    return true;
                }
            }
            b_pointer++;
        }
        return false;
    }
};