class Solution {
public:
    int hIndex(vector<int>& citations) {
        if(citations.size() == 0) return 0;
        sort(citations.begin(), citations.end());
        int h = 0;
        for(int i = citations.size() - 1; i >= 0; i--){
            if(citations.size() - i <= citations[i]){
                h++;
                //is_found = true;
            }
        }
        return h;
    }
}; 