class Solution {
public:
    
    
    bool isNStraightHand(vector<int>& hand, int W) {
        if(hand.size() == 0 && W == 0) return true;
        if(W == 0) return false;
        if(hand.size() % W != 0) return false;
        sort(hand.begin(), hand.end());
        bool handFound = true;
        int sets = hand.size() / W;
        int setCount = 0;
        while(handFound){
            //try to find new hand
            int card_count = 0;
            int prev = -1;
            for(int i = 0;i < hand.size(); i++){
                if(hand[i] != -1 && card_count == 0) {
                    prev = hand[i];
                    hand[i] = -1;
                    card_count++;
                } else {
                    if(hand[i] == prev + 1){
                        prev = hand[i];
                        hand[i] = -1;
                        card_count++;
                    }
                }
                if(card_count == W) break;
                if(i == hand.size() - 1 && card_count < W) handFound = false;
            }
            if(handFound)
                setCount++;
        }
        return sets == setCount;    
    }
};