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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root == nullptr){
            return result;
        }
        int level = 0;
        queue<TreeNode*> q1;
        //stack<TreeNode*> s;
        queue<TreeNode*> q2;
        
        q1.push(root);
        level += 1;
        vector<int> levelContainer;
        while(!q1.empty() || !q2.empty()){
            if(level % 2 == 1){ //go left to right
                if(q1.empty()){
                    //proceed to next level
                    result.push_back(levelContainer);
                    levelContainer.clear(); 
                    level += 1;
                } else {
                    TreeNode* current = q1.front();
                    if(current -> left != nullptr){
                        q2.push(current -> left);
                    }
                    if(current -> right != nullptr){
                        q2.push(current -> right);
                    }
                    levelContainer.push_back(current -> val);
                    cout << current -> val << "is taken from queue" << endl;
                    q1.pop();
                }
            } else { //go right to left
                if(q2.empty()){
                    //proceed to next level
                    //reverse the container before pushing
                    reverse(levelContainer.begin(), levelContainer.end());
                    result.push_back(levelContainer);
                    levelContainer.clear();
                    level += 1;
                } else {
                    TreeNode* current = q2.front();
                    if(current -> left != nullptr){
                        q1.push(current -> left);
                    }
                    if(current -> right != nullptr){
                        q1.push(current -> right);
                    }
                    levelContainer.push_back(current -> val);
                    cout << current -> val << "is taken from stack" << endl;
                    q2.pop();
                }
            }
        }
        if(level % 2 == 0)
            reverse(levelContainer.begin(), levelContainer.end());
        result.push_back(levelContainer);
        return result;        
    }
};