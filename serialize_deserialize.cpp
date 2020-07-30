#include <bits/stdc++.h>
using namespace std;


struct TreeNode{
    int val; 
    TreeNode* left;
    TreeNode* right;
};

//length of the string will give number of nodes
string inorder(TreeNode* root, string result){
    //check if leaf node:
    if(root -> left == nullptr && root -> right == nullptr){
        result += root -> val;
        return result; //nothing else to explore
    }
    
    //left
    if(root -> left != nullptr){
        result += inorder(root -> left, result);
    }
    
    //root
    result += root -> val + "*"; // we need to separate the data
    
    //right
    if(root -> right != nullptr){
        result += inorder(root -> right, result);
    }
    return result;
}

//length of the string will give number of nodes
string preorder(TreeNode* root, string result){ 
    //root, left, right
    //check if leaf node:
    if(root -> left == nullptr && root -> right == nullptr){
        result += root -> val;
        return result; //nothing else to explore
    }
      
    //root
    result += root -> val + "*"; // we need to separate the data
    
    //left
    if(root -> left != nullptr){
        result += preorder(root -> left, result);
    }
    
    //right
    if(root -> right != nullptr){
        result += preorder(root -> right, result);
    }
    return result;
}

TreeNode* deserialize(string data){
    //number of nodes will be length of data / 2
    int length = data.size();
    int num_nodes = length / 2;
    //first half will be preorder, second half will be inorder
    string pre_order = data.substr(0, num_nodes);
    string in_order = data.substr(num_nodes, num_nodes);
    vector<int> preorder = split_data(pre_order);
    vector<int> inorder = split_data(in_order);
    return buildBinaryTree(preorder, inorder);
}

TreeNode* generateBinaryTree(int root_index, int in_start, int in_end, vector<int> pre_order, vector<int> in_order){
    if(in_start > in_end || root_index > pre_order.size()){
        return nullptr;
    }
    TreeNode* root = new TreeNode();
    root -> val = pre_order[root_index];
   
    //find the position of this root in the in_order
    int root_pos = 0;
    for(int i = 0; i < in_order.size(); i++){
        if(in_order[i] == pre_order[root_index]){
            root_pos = i;
            break;
        }
    }
    
    // root_pos (4) = 
    // in_order = 
    
    // left sub tree                                
    root -> left = generateBinaryTree(root_index + 1, in_start, root_pos - 1, vector<int> pre_order, vector<int> in_order);
    
    //      1
    //  2       4 
    //null 5 6    7
    // serialize -> 1*2*5*4*6*7*  2*5*1*6*4*7* => 16 / 2 => 8
//-->      1*2*500*4*2*500*4*1* =>
    
    
    // right sub tree
    root -> right = generateBinaryTree(root_index + root_pos - in_start + 1, root_pos + 1, in_end, pre_order, in_order);
                                       
    return root;                                      
}

TreeNode* buildBinaryTree(vector<int> pre_order, vector<int> inorder){
    // the first node in pre_order is always root
    if(pre_order.size() == 0){
        return nullptr; // no tree
    }
    
    return generate BinaryTree

    // find the position of this root in the in_order string -> left sub tree, right_sub tree
    
}


// this method will split the data and return a vector of ints where * occurs
vector<int> split_data(string ordering){
    vector<int> result;
    if(ordering.size() == 0) return result;
    
    int start = 0;
    int length = 0;
    for(int i = 0; i < ordering.size(); i++){
        // There will always be a * at the back of the parsed ordering data
        if(ordering[i] == '*'){
            result.push_back(stoi(ordering.substr(start, length)));
            start = i+1;
            length = 0; // reset the length
        } else {
            length++;
        }
    }
    return result;
}
    
    
//      1
//  2      4 
//null 500 null null

// serialize -> 1*2*5*4*  2*5*4*1* => 16 / 2 => 8
//-->      1*2*500*4*2*500*4*1* =>
string serialize(TreeNode* root){
    // do pre order traversal 
    string pre_order = preorder(root, "");
    // do in order traversal
    string in_order = inorder(root, "");
    
    return pre_order + in_order; // serialized data
}

#include <iostream>

using namespace std;

int main(){

    
    return 0;
}
