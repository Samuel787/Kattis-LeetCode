class Solution {
public:
    string removeDuplicates(string S) {
        stack<char> mStack;
        for(int i = 0; i < S.size(); i++){
            if(mStack.empty()){
                mStack.push(S[i]);
            } else {
                if(mStack.top() == S[i]){
                    mStack.pop();
                } else {
                    mStack.push(S[i]);
                }
            }
        }
        string result = "";
        while(!mStack.empty()){
            result += mStack.top();
            mStack.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
    
};