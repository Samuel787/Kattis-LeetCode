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
    
    TreeNode* pruneTree(TreeNode* root) {
        bool val = containsOne(root);
        if(val) return root;
        return nullptr;
    }
    
    bool containsOne(TreeNode* root){
        if(root == nullptr) return nullptr;
        
        bool leftContainsOne = containsOne(root -> left);
        bool rightContainsOne = containsOne(root -> right);
        
        if(!leftContainsOne) root -> left = nullptr;
        if(!rightContainsOne) root -> right = nullptr;
        
        return root -> val == 1 || leftContainsOne || rightContainsOne;
    }
};