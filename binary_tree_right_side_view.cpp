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
    
    struct Leveled_nodes{
        TreeNode* node;
        int level;
    };
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> results;
        if(root == nullptr){
            return results;
        }
        queue<Leveled_nodes> q;
        vector<Leveled_nodes> mList;
        Leveled_nodes ln = {root, 0};
        q.push(ln);
        while(!q.empty()){
            Leveled_nodes curr = q.front();
            q.pop();
            mList.push_back(curr);
            if(curr.node -> left != nullptr){
                q.push({curr.node -> left, curr.level + 1});
            }
            if(curr.node -> right != nullptr){
                q.push({curr.node -> right, curr.level + 1});
            }
        }
        
        Leveled_nodes prev_node = mList[0];
        results.push_back(prev_node.node -> val);
        for(int i = 1; i < mList.size(); i++){
            Leveled_nodes curr = mList[i];
            if(curr.level > prev_node.level && prev_node.level != 0){
                results.push_back(prev_node.node -> val);
            }
            prev_node = curr;
        }
        if(mList.size() > 1){
            results.push_back(mList[mList.size() - 1].node -> val);
        }
        return results;
    }
};