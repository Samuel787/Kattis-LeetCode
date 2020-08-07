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
    
    
    struct Node{
        TreeNode* node;
        int vd;
        int hd;
    };
    
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        
        vector<vector<int>> results;
        if(root == nullptr) return results;
        
        map<int, vector<Node*>> data; // maps horizontal vals -> columns 
        
        queue<Node*> q;
        Node* rNode = new Node();
        rNode -> node = root;
        rNode -> vd = 1000; // max height possible? idk
        rNode -> hd = 1000;
        q.push(rNode);
        while(!q.empty()){
            Node* curr_node = q.front();
            data[curr_node -> hd].push_back(curr_node);
            if(curr_node -> node -> left != nullptr){
                Node* leftNode = new Node();
                leftNode -> node = curr_node -> node-> left;
                leftNode -> vd = curr_node -> vd - 1;
                leftNode -> hd = curr_node -> hd - 1;
                q.push(leftNode);
            }
            
            if(curr_node -> node -> right != nullptr){
                Node* rightNode = new Node();
                rightNode -> node = curr_node -> node -> right;
                rightNode -> vd = curr_node -> vd - 1;
                rightNode -> hd = curr_node -> hd + 1;
                q.push(rightNode);
            }
            
            q.pop();    
        }
        
        map<int, vector<Node*>>::iterator it;
        for(it = data.begin(); it != data.end(); it++){
            //each column
            vector<int> column;
            vector<pair<int, int>> temp;
            for(int i = 0; i < (it -> second).size(); i++){
                Node* mNode = (it -> second)[i];
                temp.push_back(make_pair(1000 - mNode -> vd, mNode -> node -> val));
            }
            sort(temp.begin(), temp.end());
            for(int i = 0; i < temp.size(); i++){
                column.push_back(temp[i].second);
            }
            results.push_back(column);
        }
        return results;
    }
};