class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        if(rooms.size() <= 1) return true;
        vector<bool> all_rooms(rooms.size(), 0);
        queue<int> keys;
        keys.push(0);
        while(!keys.empty()){
            int key = keys.front();
            //cout << key << endl;
            keys.pop();
            if(all_rooms[key] == true) continue;
            all_rooms[key] = true;
            for(int k : rooms[key]){
                keys.push(k);
            }
        }
        
        for(bool x : all_rooms){
            if(!x) return x;
        }
        return true;
    }
};