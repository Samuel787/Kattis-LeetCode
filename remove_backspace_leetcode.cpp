class Solution {
public:
    
    string removeBackspace(string input){
        stack<char> result;
        for(int i = 0; i < input.size(); i++){
            if(input[i] == '#'){
                if(!result.empty()){
                    result.pop();
                }
            } else {
                result.push(input[i]);
            }
        }
        
        //build output
        string output = "";
        while(!result.empty()){
            output += result.top();
            result.pop();
        }
        return output;
    }
    
    bool backspaceCompare(string S, string T) {
        return removeBackspace(S) == removeBackspace(T);
    }
};