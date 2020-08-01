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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode* node;
        if(t1 != nullptr && t2 != nullptr){
            node = new TreeNode(t1 -> val + t2 -> val);
            node -> left = mergeTrees(t1 -> left, t2 -> left);
            node -> right = mergeTrees(t1 -> right, t2 -> right);
        }
        if(t1 != nullptr && t2 == nullptr){
            node = new TreeNode(t1 -> val);
            node -> left = mergeTrees(t1 -> left, nullptr);
            node -> right = mergeTrees(t1 -> right, nullptr);
        }
        if(t1 == nullptr && t2 == nullptr){
            return nullptr; //terminate the recursion
        }
        if(t1 == nullptr && t2 != nullptr){
            node = new TreeNode(t2 -> val);
            node -> left = mergeTrees(nullptr, t2 -> left);
            node -> right = mergeTrees(nullptr, t2 -> right);
        }
        return node;
    }
};