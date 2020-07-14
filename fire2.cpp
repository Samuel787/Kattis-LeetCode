#include <bits/stdc++.h>
using namespace std;

struct state{
    int steps;
    int width;
    int height;
    int y;
    int x;

    bool operator <(const state & playerObj) const
    {
        return x < playerObj.x;
    }
};

/*
    Next state of the map with the @ at the same position
*/
vector<string> next_map(vector<string> map, int height, int width){
    char new_fire = '^';
    // vector<string> map = curr.map;
    // int height = curr.height;
    // int width = curr.width;
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(map[i][j] == '*'){
                //spread the fire
                //up
                if(i-1 >= 0 && map[i-1][j] != '*' && map[i-1][j] != '#'){
                    map[i-1][j] = new_fire;
                }
                //down
                if(i+1 < height && map[i+1][j] != '*' && map[i+1][j] != '#'){
                    map[i+1][j] = new_fire;
                }
                //left
                if(j-1 >= 0 && map[i][j-1] != '*' && map[i][j-1] != '#'){
                    map[i][j-1] = new_fire;
                }
                //right
                if(j+1 < width && map[i][j + 1] != '*' && map[i][j+1] != '#'){
                    map[i][j+1] = new_fire;
                }
            }
        }
    }

    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(map[i][j] == '^'){
                map[i][j] = '*';
            }
        }
    }

    return map;
}

/*
    generates all the 4 neighbours
*/
vector<state> generate_neighbours(state curr, vector<string> new_map){
    //assert: @ is not at the border
    vector<state> new_states;
    //vector<string> new_map = next_map(curr);
    int new_x, new_y;
    
    //goes up
    new_y = curr.y - 1;
    new_x = curr.x;
    if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
        vector<string> up_map = new_map;
        up_map[new_y][new_x] = '@';
        new_states.push_back({curr.steps + 1, curr.width, curr.height, new_y, new_x});
    }
    
    //goes down
    new_y = curr.y + 1;
    new_x = curr.x;
    if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*' ){
        vector<string> up_map = new_map;
        up_map[new_y][new_x] = '@';
        new_states.push_back({curr.steps + 1, curr.width, curr.height, new_y, new_x});
    }
    
    //goes left
    new_y = curr.y;
    new_x = curr.x - 1;
    if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
        vector<string> up_map = new_map;
        up_map[new_y][new_x] = '@';
        new_states.push_back({curr.steps + 1, curr.width, curr.height, new_y, new_x});
    }
    
    //goes right
    new_y = curr.y;
    new_x = curr.x + 1;
    if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
        vector<string> up_map = new_map;
        up_map[new_y][new_x] = '@';
        new_states.push_back({curr.steps + 1, curr.width, curr.height, new_y, new_x});
    }
    return new_states;
}

/**
 *  returns true when you have reached the border. false otherwise
 */
bool check_state(state curr){
    if(curr.y == 0 || curr.x == 0 || curr.y == curr.height - 1 || curr.x == curr.width - 1){
        return true;
    }
    return false;
}

pair<int, int> get_pos(vector<string> map, int width, int height){
    for(int i = 0; i < height; i++){
        for(int j = 0; j < width; j++){
            if(map[i][j] == '@'){
                return make_pair(i, j);
            }
        }
    }
    return make_pair(-1, -1);
}

int main(){
    int N;
    cin >> N;
    while(N--){
        int w;
        int h;
        cin >> w;
        cin >> h;
        int x, y;
        bool found = false;
        vector<vector<string>> all_maps;
        vector<string> map(h, "");
        for(int i = 0; i < h; i++){
            cin >> map[i];
        }
        all_maps.push_back(map);
        queue<state> q;
        pair<int, int> initial_pos = get_pos(map, w, h);
        state initial = {1, w, h, initial_pos.first, initial_pos.second};
        q.push(initial);
        set<pair<int, int>> visited;
        while(!q.empty() ){
            state curr = q.front();
            if(check_state(curr)){
                found = true;
                cout << curr.steps << endl;
                break;
            }
            q.pop();
            if(visited.find(make_pair(curr.x, curr.y)) != visited.end()){
                continue;
            }
            visited.insert(make_pair(curr.x, curr.y));

            vector<state> new_states;
            if(curr.steps == all_maps.size()){
                all_maps.push_back(next_map(all_maps[all_maps.size() - 1], h, w));
            }
            new_states = generate_neighbours(curr, all_maps[curr.steps]);
            for(int i = 0; i < new_states.size(); i++){
                if(visited.find(make_pair(new_states[i].x, new_states[i].y)) == visited.end()){
                    q.push(new_states[i]);
                }
            }
        }
        if(!found){
            cout << "IMPOSSIBLE" << endl;
        }
    }
}


// #include <bits/stdc++.h>
// using namespace std;

// struct state{
//     vector<string> map;
//     int steps;
//     int width;
//     int height;
//     int y;
//     int x;

//     bool operator <(const state & playerObj) const
//     {
//         return x < playerObj.x;
//     }
// };

// /*
//     Next state of the map with the @ at the same position
// */
// vector<string> next_map(state curr){
//     char new_fire = '^';
//     vector<string> map = curr.map;
//     int height = curr.height;
//     int width = curr.width;
//     for(int i = 0; i < height; i++){
//         for(int j = 0; j < width; j++){
//             if(map[i][j] == '*'){
//                 //spread the fire
//                 //up
//                 if(i-1 >= 0 && map[i-1][j] != '*' && map[i-1][j] != '#'){
//                     map[i-1][j] = new_fire;
//                 }
//                 //down
//                 if(i+1 < height && map[i+1][j] != '*' && map[i+1][j] != '#'){
//                     map[i+1][j] = new_fire;
//                 }
//                 //left
//                 if(j-1 >= 0 && map[i][j-1] != '*' && map[i][j-1] != '#'){
//                     map[i][j-1] = new_fire;
//                 }
//                 //right
//                 if(j+1 < width && map[i][j + 1] != '*' && map[i][j+1] != '#'){
//                     map[i][j+1] = new_fire;
//                 }
//             }
//         }
//     }

//     for(int i = 0; i < height; i++){
//         for(int j = 0; j < width; j++){
//             if(map[i][j] == '^'){
//                 map[i][j] = '*';
//             }
//         }
//     }

//     return map;
// }

// /*
//     generates all the 4 neighbours
// */
// vector<state> generate_neighbours(state curr){
//     //assert: @ is not at the border
//     vector<state> new_states;
//     vector<string> new_map = next_map(curr);
//     int new_x, new_y;
    
//     //goes up
//     new_y = curr.y - 1;
//     new_x = curr.x;
//     if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
//         vector<string> up_map = new_map;
//         up_map[new_y][new_x] = '@';
//         new_states.push_back({up_map, curr.steps + 1, curr.width, curr.height, new_y, new_x});
//     }
    
//     //goes down
//     new_y = curr.y + 1;
//     new_x = curr.x;
//     if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*' ){
//         vector<string> up_map = new_map;
//         up_map[new_y][new_x] = '@';
//         new_states.push_back({up_map, curr.steps + 1, curr.width, curr.height, new_y, new_x});
//     }
    
//     //goes left
//     new_y = curr.y;
//     new_x = curr.x - 1;
//     if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
//         vector<string> up_map = new_map;
//         up_map[new_y][new_x] = '@';
//         new_states.push_back({up_map, curr.steps + 1, curr.width, curr.height, new_y, new_x});
//     }
    
//     //goes right
//     new_y = curr.y;
//     new_x = curr.x + 1;
//     if(new_map[new_y][new_x] != '#' && new_map[new_y][new_x] != '*'){
//         vector<string> up_map = new_map;
//         up_map[new_y][new_x] = '@';
//         new_states.push_back({up_map, curr.steps + 1, curr.width, curr.height, new_y, new_x});
//     }
//     return new_states;
// }

// /**
//  *  returns true when you have reached the border. false otherwise
//  */
// bool check_state(state curr){
//     if(curr.y == 0 || curr.x == 0 || curr.y == curr.height - 1 || curr.x == curr.width - 1){
//         return true;
//     }
//     return false;
// }

// pair<int, int> get_pos(vector<string> map, int width, int height){
//     for(int i = 0; i < height; i++){
//         for(int j = 0; j < width; j++){
//             if(map[i][j] == '@'){
//                 return make_pair(i, j);
//             }
//         }
//     }
//     return make_pair(-1, -1);
// }

// int main(){
//     int N;
//     cin >> N;
//     while(N--){
//         int w;
//         int h;
//         cin >> w;
//         cin >> h;
//         int x, y;
//         bool found = false;
//         vector<string> map(h, "");
//         for(int i = 0; i < h; i++){
//             cin >> map[i];
//         }
//         queue<state> q;
//         pair<int, int> initial_pos = get_pos(map, w, h);
//         state initial = {map, 1, w, h, initial_pos.first, initial_pos.second};
//         q.push(initial);
//         set<pair<int, int>> visited;
//         while(!q.empty() ){
//             state curr = q.front();
//             if(check_state(curr)){
//                 found = true;
//                 cout << curr.steps << endl;
//                 break;
//             }
//             q.pop();
//             if(visited.find(make_pair(curr.x, curr.y)) != visited.end()){
//                 continue;
//             }
//             visited.insert(make_pair(curr.x, curr.y));
//             vector<state> new_states = generate_neighbours(curr);
//             for(int i = 0; i < new_states.size(); i++){
//                 if(visited.find(make_pair(new_states[i].x, new_states[i].y)) == visited.end()){
//                     q.push(new_states[i]);
//                 }
//             }
//         }
//         if(!found){
//             cout << "IMPOSSIBLE" << endl;
//         }
//     }
// }