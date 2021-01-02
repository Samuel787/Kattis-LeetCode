/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if(original -> val == target -> val){
            return cloned;
        } 
        if(original -> left == nullptr && original -> right == nullptr){
            return nullptr;
        }
        if(original -> left != nullptr){
            TreeNode* res = getTargetCopy(original -> left, cloned -> left, target);
            if(res != nullptr){
                return res;
            }
        }
        if(original -> right != nullptr){
            TreeNode* res = getTargetCopy(original -> right, cloned -> right, target);
            if(res != nullptr){
                return res;
            }
        }
        return nullptr;
        
    }
};