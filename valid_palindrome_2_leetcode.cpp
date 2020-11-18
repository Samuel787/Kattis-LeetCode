class Solution {
public:
    bool validPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;
        bool has_deleted = false;
        while(start < end){
            if(s[start] == s[end]){
                start++;
                end--;
            } else {
                bool res1 = false;
                bool res2 = false;
                int start1 = start + 1;
                int start2 = start;
                int end1 = end;
                int end2 = end - 1;
                while(start1 < end1){
                    if(s[start1] == s[end1]){
                        start1++;
                        end1--;
                    } else {
                        res1 = false;
                        break;
                    }
                }
                if(start1 >= end1){
                    res1 = true;
                    return true;
                }
                while(start2 < end2){
                    if(s[start2] == s[end2]){
                        start2++;
                        end2--;
                    } else {
                        res2 = false;
                        break;
                    }
                }
                if(start2 >= end2){
                    return true;
                }
                return false;
            }
        }
        return true;
    }
};