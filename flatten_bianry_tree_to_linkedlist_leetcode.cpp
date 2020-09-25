/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    void flatten(TreeNode* root) {
        if(root == nullptr){
            return;
        }
        stack<TreeNode*> mStack;
        mStack.push(root);
        
        while(!mStack.empty()){
            TreeNode* curr_node = mStack.top();
            mStack.pop();
            if(curr_node -> right != nullptr){
                mStack.push(curr_node -> right);
            }
            if(curr_node -> left != nullptr){
                mStack.push(curr_node -> left);
            }
            if(!mStack.empty()){
                curr_node -> right = mStack.top();
            }
            curr_node -> left = nullptr;
        }
    }
    
};