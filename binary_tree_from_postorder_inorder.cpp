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
    
    TreeNode* createTree(int postindex, int in_start, int in_end, vector<int>& inorder, vector<int>& postorder){
        if(in_start > in_end){
            return nullptr;
        }
        
        TreeNode* root = new TreeNode(0);
        root -> val = postorder[postindex];
        
        int inRoot;
        for(int i = in_start; i <= in_end; i++){
            if(inorder[i] == postorder[postindex]){
                inRoot = i;
                break;
            }
        }
        
        root -> right =  createTree(postindex - 1, inRoot + 1, in_end, inorder, postorder);
        root -> left = createTree(postindex - (in_end - inRoot) - 1, in_start, inRoot - 1, inorder, postorder);
        
        return root;    
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return createTree(postorder.size() - 1, 0, inorder.size()-1, inorder, postorder);
    }
};