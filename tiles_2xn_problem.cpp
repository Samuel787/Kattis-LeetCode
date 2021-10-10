#include <bits/stdc++.h>
using namespace std;

int problem(int m)
{
    if (m <= 0)
    {
        return 0;
    }
    else if (m == 1)
    {
        return 1;
    }
    else
    {
        return problem(m - 1) + problem(m - 2);
    }
}

int main()
{
    cout << problem(3) << endl;
    return 0;
}