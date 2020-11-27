class Solution {
public:
    bool isValid(string s) {
        stack<char> mStack;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == ')'){
                if(!mStack.empty() && mStack.top() == '('){
                    mStack.pop();
                } else {
                    return false;
                }
            } else if(s[i] == ']'){
                if(!mStack.empty() && mStack.top() == '['){
                    mStack.pop();
                } else {
                    return false;
                }
            } else if(!mStack.empty() && s[i] == '}'){
                if(mStack.top() == '{'){
                    mStack.pop();
                } else {
                    return false;
                }
            } else {
                mStack.push(s[i]);
            }
        }
        return mStack.empty();
    }
};