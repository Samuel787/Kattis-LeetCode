// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    
    // [good, good, good, good, bad, bad]
    int getFirstBad(long start, long end){
        
        long mid = (end + start) / 2;
        
        bool result = isBadVersion(mid);
        
        if(mid == 1){ //base case for the recursion
            // -> end must be 1
            if(result){
                return mid;
            } else {
                return mid + 1;
            }
        }
        if(result){
            if(!isBadVersion(mid - 1)){
                return mid;
            } else {
                //recurse on the left side
                return getFirstBad(start, mid - 1);
            }
        } else {
            //not bad 
            if(isBadVersion(mid + 1)){
                return (mid + 1);
            } else {
                // recurse on the right side
                return getFirstBad(mid + 1, end);
            }
        }
    }
    
    int firstBadVersion(int n) {
        return getFirstBad(1, n);
    }
};