#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    stack<int> mpile;
    stack<int> apile;

    int sock;
    int num_socks = n*2;
    
    for(int i = 0; i < num_socks; i++){
        cin >> sock;
        mpile.push(sock);
    }


    //begin simulation
    /**
     * We only have to move the socks from main pile to the auxi pile 
     * and check if the top socks match after every action once.
     */
    int actions = 0;
    while(!mpile.empty()){
        //take one sock put it into auxilary pile
        sock = mpile.top();
        mpile.pop();
        apile.push(sock);
        bool remove = true;
        actions++;
        while(remove && !mpile.empty() && !apile.empty()){
            if(mpile.top() == apile.top()){
                mpile.pop();
                apile.pop();
                //she can remove now
                actions++;
            } else {
                remove = false;
            }
        }
    }
    
    if(apile.size() == 0){
        cout << actions << endl;
    } else {
        cout << "impossible" << endl;
    }
}