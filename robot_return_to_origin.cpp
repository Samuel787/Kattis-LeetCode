class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0;
        int y = 0;
        for(char X : moves){
            switch(X){
                case 'R':
                    x++;
                    break;
                case 'L':
                    x--;
                    cout << "Meow " << x <<  endl;
                    break;
                case 'U':
                    y++;
                    break;
                case 'D':
                    y--;
                    break;
            }
        }
        cout << x << " "<< y << endl;
        return (x == 0 && y == 0);
    }
};