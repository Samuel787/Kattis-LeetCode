class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<tuple<int, int>> info;
        int numRows = mat.size();
        int numCols = mat[0].size();
        for(int i = 0; i < numRows; i++){
            int count = 0;
            while(count < numCols && mat[i][count] == 1) count++;
            info.push_back(make_tuple(count, i));
        }
        sort(info.begin(), info.end());
        vector<int> result;
        for(int i = 0; i < k; i++){
            result.push_back(get<1>(info[i]));
        }
        return result;
    }
};
