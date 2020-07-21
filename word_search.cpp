#include <bits/stdc++.h>
using namespace std;

    void print_map(vector<vector<char>> board){
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[0].size(); j++){
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        cout << endl;
    }
    bool validPos(int width, int height, int x, int y){
        if(x < 0 || y < 0 || y > height - 1 || x > width - 1){
            return false;
        }
        return true;
    }

    
    bool search_new(vector<vector<char>> &board, string word, int x, int y, int height, int width){
        if(word == ""){
            return true;
        }
        if(board[y][x] != word[0]){
            print_map(board);
            cout << "return false because " << board[y][x] << "not start of " << word << endl;
            return false;
        }
        if(word.size() == 1) return true;
        string new_word = word.substr(1, word.size()-1);
        board[y][x] = '-';
        //search up
        //search down
        //search left
        //search right
        int new_x; int new_y;
        new_x = x; new_y = y - 1;
        if(validPos(width, height, new_x, new_y)){
            if(search_new(board, new_word, new_x, new_y, height, width)){
                return true;
            } else {
               // board[new_y][new_x] = word[1];
            }
        }
        new_x = x; new_y = y + 1;
        if(validPos(width, height, new_x, new_y)){
            if(search_new(board, new_word, new_x, new_y, height, width)){
                return true;
            } else {
                //board[new_y][new_x] = word[1];
            }
        }
        new_x = x-1; new_y = y;
        if(validPos(width, height, new_x, new_y)){
            if(search_new(board, new_word, new_x, new_y, height, width)){
                return true;
            } else {
                //board[new_y][new_x] = word[1];
            }
        }
        new_x = x+1; new_y = y;
        if(validPos(width, height, new_x, new_y)){
            if(search_new(board, new_word, new_x, new_y, height, width)){
                return true;
            } else {
                //board[new_y][new_x] = word[1];
            }
        }
        board[y][x] = word[0];
        print_map(board);
        cout << "returning false as there is no continuation at " << board[y][x] << endl;
        return false;   
    }
    
    bool exist(vector<vector<char>> &board, string word) {
        int height = board.size();
        if(height == 0) return false;
        int width = board[0].size();
        if(width == 0) return false;
        
        for(int i = 0; i < height; i++){
            for(int j = 0; j < width; j++){
                vector<vector<char>> tempBoard = board;
                //char temp = board[i][j];
                if(search_new(tempBoard, word, j, i, height, width)){
                    return true;
                } else {
                    //board[i][j] = temp;
                }
            }
        }
        return false;
    }

/*
    Driver code
*/
int main(){
    vector<vector<char>> map{{'a', 'b'}, {'c', 'd'}};
    string word = "cdba";
    cout << exist(map, word) << endl;

}