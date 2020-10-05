class Solution {
public:
    int numJewelsInStones(string J, string S) {
        unordered_set<char> jewels;
        for(char x: J){
            jewels.insert(x);
        }
        int count = 0;
        for(char y : S){
            if(jewels.find(y) != jewels.end()){
                count++;
            }
        }
        return count;
    }
};