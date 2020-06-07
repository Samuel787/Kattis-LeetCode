#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/***
    In this snake game, i have represented up direction as 0, down as 1,
    right as 3, left as 2.
*/

/*
  This method determines the actual direction the snake moves in the next step
*/
int convert_instruction(char dir, int curr_dir){
    if(dir == 'F' || dir == 'E'){
        //continue moving in same direction
        return curr_dir;
    } else if (dir == 'L'){
        if(curr_dir == 0){
            return 2;
        } else if(curr_dir == 1){
            return 3;
        } else if(curr_dir == 2){
            return 1;
        } else if(curr_dir == 3){
            return 0;
        }
    } else if (dir == 'R'){
        if(curr_dir == 0){
            return 3;
        } else if (curr_dir == 1){
            return 2;
        } else if (curr_dir == 2){
            return 0;
        } else if (curr_dir == 3){
            return 1;
        }
    }
    return -1;
}

/**
  This represents a unit of the snake
*/
struct Body{
    int x;
    int y;
};


/**
  @param snake vector of Body representing the snake
  @return This method returns true if the snake hits itself.
  It returns false otherwise.
*/
bool check_collision(vector<Body> snake){
    // //naive method
    // for(int i = 0; i < snake.size(); i++){
    //     for(int j = i+1; j < snake.size(); j++){
    //         if(snake[i].x == snake[j].x && snake[i].y == snake[j].y){
    //             return true;
    //         }
    //     }
    // }
    // return false;

    set<pair<int, int>> bag;
    for(int i = 0; i < snake.size(); i++){
        auto result = bag.insert(make_pair(snake[i].x, snake[i].y));
        if(!result.second){
            return true;
        }
    }
    return false;
}

int main(void)
{
    int t;
    cin >> t;
    //create new game and simulate
    while(t > 0){
        int n;
        cin >> n;
        //create snake
        vector<Body> snake;
        struct Body head;
        head.x = 0;
        head.y = 0;
        snake.push_back(head);
        string instruction;
        cin >> instruction;
        
        int driver = 0; //let the initial direction be up
        bool collide = false;
        for(int i = 0; i < n; i++){
            char mov;
            mov = instruction[i];
            //get the next direction of the snake
            driver = convert_instruction(mov, driver);
            //new position of the head
            struct Body newHead;
            if(driver == 0){
                newHead.x = snake[snake.size() - 1].x;
                newHead.y = snake[snake.size() - 1].y + 1;
            } else if (driver == 1){
                newHead.x = snake[snake.size() - 1].x;
                newHead.y = snake[snake.size() - 1].y - 1;
            } else if (driver == 2){
                newHead.x = snake[snake.size() - 1].x - 1;
                newHead.y = snake[snake.size() - 1].y;
            } else if (driver == 3){
                newHead.x = snake[snake.size() - 1].x + 1;
                newHead.y = snake[snake.size() - 1].y;
            } else {
                return -1; //invalid input
            }

            snake.push_back(newHead);
            if(mov != 'E'){
                //remove old tail
                snake.erase(snake.begin());
            }

            //print out head position just to check
            //cout << snake[snake.size()-1].x << " " << snake[snake.size()-1].y << endl;

            //check collision
            collide = check_collision(snake);
            if(collide){
                cout << i+1 << endl;
                break; //next test case
            }
        }
        if(!collide){
            cout << "YES" << endl;
        }
        t--;
    }
    return 0;
}