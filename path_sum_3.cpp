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
    
    int count = 0;
    vector<int> nodes;
    
    void helper(TreeNode* root, int sum){
        if(root == nullptr){
            return;
        }
        
        nodes.push_back(root -> val);
        
        helper(root -> left, sum);
        helper(root -> right, sum);
        
        int currSum = 0;
        for(int i =nodes.size() - 1; i >= 0; i--){
            currSum += nodes[i];
            if(currSum == sum){
                count++;
            }
        }
        
        nodes.erase(nodes.begin() + nodes.size() - 1);
    }
    int pathSum(TreeNode* root, int sum) {
        helper(root, sum);
        return count;
    }
};