/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        if(root == nullptr)
            return result;
        
        vector<Node*> mChildren = root -> children;
        for(int i = 0; i < mChildren.size(); i++){
            vector<int> cResult = postorder(mChildren[i]);
            result.insert(result.end(), cResult.begin(), cResult.end());
        }
        result.push_back(root -> val);
        return result;
    }
};