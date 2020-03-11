#include <bits/stdc++.h>
using namespace std;

/** PROBLEM STATEMENT
Given a floor of size n x m and tiles of size 1 x m. The problem is to count the number of ways to tile the given floor using 1 x m tiles. A tile can either be placed horizontally or vertically.
Both n and m are positive integers and 2 < = m.
*
*/

int count_ways(int n, int m){
    if(n < m){
        return 1;
    } else if (n == m){
        return 2;
    } else {
        return count_ways(n-1, m) + count_ways(n-m, m);
    }
}

int main(){

    int n;
    int m;
    cin >> n;
    cin >> m;

    cout << count_ways(7, 4);
}