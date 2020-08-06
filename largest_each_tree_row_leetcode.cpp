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
    vector<int> largestValues(TreeNode* root) {
        
        queue<TreeNode*> q;
        q.push(root);
        q.push(nullptr); //nullptr is my token
        vector<int> results;
        vector<int> row;
        if(root == nullptr) return results;
        row.push_back(root -> val);
        while(!q.empty()){
            TreeNode* curr = q.front();
            q.pop();
            row.push_back(curr -> val);
            //cout << "I'm pushing " << curr -> val << endl;
            if(curr -> left != nullptr){
                q.push(curr -> left);
            }
            if(curr -> right != nullptr){
                q.push(curr -> right);
            }
            if(q.front() == nullptr){
                q.pop();
                int max = INT_MIN;
                for(int i = 0; i < row.size(); i++){
                    if(row[i] > max) max = row[i];
                }
                results.push_back(max);
                row.clear();
                if(q.empty()) break;
                q.push(nullptr);                
            }
        }
        return results;
    }
};