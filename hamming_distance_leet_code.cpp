class Solution {
public:
    
    
    string convertToBits(int x){
        stack<char> bits;
        while(x > 0){
            if(x%2 == 0){
                bits.push('0');
            } else {
                bits.push('1');
            }
            x /= 2;
        }
        string result = "";
        while(!bits.empty()){
            result += bits.top();
            bits.pop();
        }
        return result;
    }
    
    int hammingDistance(int x, int y) {
        string result1 = convertToBits(x);
        string result2 = convertToBits(y);
        int dif = result1.size()-result2.size();
        if(dif != 0){
            string padding = "";
            if(dif < 0){
                //result2 is longer, so we pad result1
                dif *= -1;
                while(dif--){
                    padding += "0";
                }
                result1 = padding + result1;
            } else {
                //result1 is longer, so we pad result2
                while(dif--){
                    padding += "0";
                }
                result2 = padding + result2;
            }
        }
        
        int count = 0;
        for(int i =0; i < result1.size(); i++){
            if(result1[i] != result2[i]){
                count++;
            }
        }
        return count;
    }
};