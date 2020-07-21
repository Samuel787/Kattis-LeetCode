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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if(root == nullptr)
            return result;
        if(root -> left != nullptr){
            vector<int> temp;
            temp = inorderTraversal(root -> left);
            result.insert(result.end(), temp.begin(), temp.end());
        }
        result.push_back(root -> val);
        if(root -> right != nullptr){
            vector<int> temp;
            temp = inorderTraversal(root -> right);
            result.insert(result.end(), temp.begin(), temp.end());
        }
        return result;
    }
};