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
    
    /*
    Returns the tree rooted at pre_start
    */
    TreeNode* createTree(int pre_start, int in_start, int in_end, vector<int>& preorder, vector<int>& inorder){
        if(pre_start > preorder.size() - 1 || in_start > in_end){
            return nullptr;
        }
        
        //struct TreeNode* root = (struct TreeNode*) malloc(sizeof(struct TreeNode));
        TreeNode* root = new TreeNode(0);
        root -> val = preorder[pre_start];
        int common;
        for(int i = in_start; i <= in_end; i++){
            if(inorder[i] == preorder[pre_start]){
                common = i;
                break;
            } 
        }
        
        root -> left = createTree(pre_start + 1, in_start, common - 1, preorder, inorder);
        root -> right = createTree(pre_start + common - in_start + 1, common + 1, in_end, preorder, inorder);
        
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size() == 0){
            return nullptr;
        }
        return createTree(0, 0, inorder.size() -1, preorder, inorder);
    }
};