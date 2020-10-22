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
    int sum = 0;
    int sumOfLeftLeaves(TreeNode* root) {
        if(root == nullptr){
            return sum;
        }
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode* curr = q.front();
            q.pop();
            if(curr -> left != nullptr){
                if(isLeaf(curr -> left)){
                    sum += curr -> left -> val;
                } else {
                    q.push(curr -> left);
                }
            } 
            if(curr -> right != nullptr){
                q.push(curr -> right);
            }
        }
        return sum;
    }
    
    bool isLeaf(TreeNode* root){
        return (root -> left == nullptr && root -> right == nullptr);
    }
};



// interpretted the question wrongly
/*

        int sum = 0;
        if(root == nullptr || (root -> left == nullptr && root -> right == nullptr)){
            return sum;
        }
        queue<TreeNode*> q;
        q.push(root);
        queue<TreeNode*> temp;
        while(!q.empty()){
            int level_size = q.size();
            for(int i = 0; i < level_size; i++){
                TreeNode* curr = q.front();
                q.pop();
                if(i == 0){
                    if(curr -> left == nullptr && curr -> right == nullptr){
                        sum += curr -> val;
                        continue;
                    }
                } 
                if(curr -> left != nullptr){
                    q.push(curr -> left);
                }
                if(curr -> right != nullptr){
                    q.push(curr -> right);
                }
            }
        }
        return sum;

*/