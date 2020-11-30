class Solution {
public:
    
    int mMax = 0;
    int totalFruit(vector<int>& tree) {
        bool terminate = false;
        for(int i = 0; i < tree.size(); i++){
            int count = 1;
            int type1 = tree[i];
            int type2 = type1;
            for(int j = i+1; j < tree.size(); j++){
                if(type1 == type2){
                    if(tree[j] == type2){
                        count++;
                    } else {
                        count++;
                        type2 = tree[j];
                    }
                } else {
                    if(tree[j] == type1 || tree[j] == type2){
                        count++;
                    } else {
                        break;
                   }
                }
                if(j == tree.size() - 1){
                    terminate = true;
                }
            }
            mMax = max(mMax, count);
            if(terminate) break;
        }
        return mMax;
    }
};