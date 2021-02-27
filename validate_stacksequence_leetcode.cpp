class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> mStack;
        for(int i = 0; i < pushed.size(); i++){
            int curr = pushed[i];
            if(popped[0] == curr){
                popped.erase(popped.begin());
                while(popped.size() != 0 && !mStack.empty() &&mStack.top() == popped[0]){
                    mStack.pop();
                    popped.erase(popped.begin());
                }
            } else {
                mStack.push(curr);
            }
        }
        return mStack.empty();
    }
};
