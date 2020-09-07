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
    int findBottomLeftValue(TreeNode* root) {
        vector<int> row;
        queue<TreeNode*> q;
        q.push(root);
        q.push(nullptr);
        int leftmost_val;
        while(!q.empty()){
            //get the first node
            TreeNode* front = q.front();
            q.pop();
            if(front == nullptr){
                if(q.empty()){
                    leftmost_val = row[0];
                    break;
                } else {
                    q.push(nullptr); //end of the current row
                    row.clear();
                    continue;
                }
            } 
            //add the children of the front node
            row.push_back(front -> val);
            if(front -> left != nullptr){
                q.push(front -> left);
            } 
            if(front -> right != nullptr){
                q.push(front -> right);
            }
        }
        return leftmost_val;   
    }
};