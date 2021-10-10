/*
// Sample code to perform I/O:

cin >> name;                            // Reading input from STDIN
cout << "Hi, " << name << ".\n";        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/

// Write your code here
#include <bits/stdc++.h>
using namespace std;

// class Node {
// public:
//     int nodeVal;
//     int priority;
//     vector<Node*> children;
//     Node() {}
//     Node(int val) {
//         nodeVal = val;
//     }
//     Node(int val, int priority, vector<Node*> children) {
//         nodeVal = val;

//     }
// }

int main()
{
    // ios::sync_with_stdio(0);
    // cin.tie(0);
    int N;
    int M;
    cin >> N;
    cin >> M;
    int distMatrix[N + 1][N + 1];
    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j <= N; j++)
        {
            if (i == j)
            {
                distMatrix[i][j] = 0;
            }
            else
            {
                distMatrix[i][j] = -1;
            }
        }
    }
    vector<int> priorities;
    priorities.push_back(0); // give node 0 the lowest priority
    // construct the priorities for the nodes
    for (int i = 0; i < N; i++)
    {
        int temp;
        cin >> temp;
        priorities.push_back(temp);
    }
    for (int i = 0; i < M; i++)
    {
        int start;
        int end;
        int dist;
        cin >> start;
        cin >> end;
        cin >> dist;
        distMatrix[start][end] = dist;
        distMatrix[end][start] = dist;
    }
    // timing vector
    vector<int> timing_vector(N + 1, 0);
    int time = 0;
    unordered_set<int> visited;
    stack<int> m_stack;
    m_stack.push(0);
    while (!m_stack.empty())
    {
        int top_node = m_stack.top();
        visited.insert(top_node);
        int next_node = -1;
        int next_dist = INT_MAX;
        int next_priority = -1;
        for (int i = 0; i < N + 1; i++)
        {
            if (i != top_node && distMatrix[top_node][i] > 0 && visited.find(i) == visited.end())
            {
                if (priorities[i] > next_priority)
                {
                    next_node = i;
                    next_dist = distMatrix[top_node][i];
                    next_priority = priorities[i];
                }
                else if (priorities[i] == next_priority && distMatrix[top_node][i] < next_dist)
                {
                    next_node = i;
                    next_dist = distMatrix[top_node][i];
                    next_priority = priorities[i];
                }
            }
        }
        if (next_node != -1)
        {
            cout << "the next node to visit from <" << top_node << "> is node <" << next_node << "> at a distance of {" << next_dist << "}" << endl;
            time += distMatrix[top_node][next_node];
            m_stack.push(next_node);
            timing_vector[next_node] = time;
            cout << "timing for node <" << next_node << "> is :" << time << endl;
        }
        else
        {
            //fully explored this node
            time += distMatrix[] cout << "fully explored" << endl;
            m_stack.pop();
        }
    }

    for (int i = 0; i < N + 1; i++)
    {
        cout << timing_vector[i + 1] << " ";
    }
    cout << endl;
}
