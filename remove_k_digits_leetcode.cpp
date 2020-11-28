class Solution {
public:
    string removeKdigits(string num, int k) {
        if(num.size() <= k){
            return "0";
        }
        for(int i = 0; i < k; i++){
            num = drop_peak(num);
            // cout << "returned" << num << endl;
        }
        if(num.size() == 0){
            return "0";
        }
        int index = 0;
        while(num[index] == '0'){
            index++;
        }
        num = num.substr(index);
        if(num == ""){
            return "0";
        }
        return num;
    }
    
    string drop_peak(string num){
        if(num.size() == 1){
            return "";
        }
        for(int i = 0; i < num.size(); i++){
            if(i == num.size()-1){
                num = num.substr(0, num.size()-1);
                return num;
            } 
            if(num[i] > num[i+1]){
                num[i] = 'x';
                break;
            }
        }
        string result = "";
        for(char x: num){
            if(x != 'x'){
                result += x;
            }
        }
        return result;
    }
};