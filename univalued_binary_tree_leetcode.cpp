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
    bool isUnivalTree(TreeNode* root) {
        if(root == nullptr){
            return true;
        }
        
        stack<TreeNode*> s;
        int num = root -> val;
        s.push(root);
        while(!s.empty()){
            TreeNode* curr = s.top();
            if(curr -> val != num){
                return false;
            }
            s.pop();
            if(curr -> left != nullptr){
                s.push(curr -> left);
            }
            if(curr -> right != nullptr){
                s.push(curr -> right);
            }
        }
        return true;
    }
};