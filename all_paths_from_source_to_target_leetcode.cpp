class Solution {
public:
    
    vector<vector<int>> dfs(vector<vector<int>>& graph, int node, vector<int> path){
        
        vector<vector<int>> all_paths;
        //case 1: target is found
        if(node == graph.size() - 1){
            path.push_back(node);
            all_paths.push_back(path);
            return all_paths;
        }
        //case 2: target not found but this path is a dead end
        if(graph[node].size() == 0){
            vector<int> new_path; //discard path and return empty path
            all_paths.push_back(new_path);
            return all_paths;
        }
        //search through all the neighbours of this node
        for(int i = 0; i < graph[node].size(); i++){
            vector<int> current_path = path;
            current_path.push_back(node);
            vector<vector<int>> node_paths = dfs(graph, graph[node][i], current_path);
            for(int j = 0; j < node_paths.size(); j++){
                all_paths.push_back(node_paths[j]);
            }
        }
        return all_paths;
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int start = 0;
        int end = graph.size() - 1;
        vector<vector<int>> all_paths;
        for(int i = 0; i < graph[0].size(); i++){
            vector<int> current_path;
            current_path.push_back(0);
            vector<vector<int>> mPaths = dfs(graph, graph[0][i], current_path);
            if(mPaths.size() != 0){
                for(int j = 0; j < mPaths.size(); j++){
                    all_paths.push_back(mPaths[j]);
                }
            }
        }
        return all_paths;
    }
};