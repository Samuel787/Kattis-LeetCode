class Solution
{
public:
    void printVector(vector<int> dummy)
    {
        string result = "";
        for (int i = 0; i < dummy.size(); i++)
        {
            result += to_string(dummy[i]) + " ";
        }
        cout << result << endl;
    }

    int maxIncreaseKeepingSkyline(vector<vector<int>> &grid)
    {
        int length = grid.size();
        if (length == 0)
        {
            return 0;
        }
        int breadth = grid[0].size();
        vector<int> x_skyline(breadth, INT_MIN);
        vector<int> y_skyline(length, INT_MIN);
        for (int i = 0; i < length; i++)
        {
            for (int j = 0; j < breadth; j++)
            {
                x_skyline[j] = max(x_skyline[j], grid[i][j]);
                y_skyline[i] = max(y_skyline[i], grid[i][j]);
            }
        }
        printVector(x_skyline);
        printVector(y_skyline);

        int sum = 0;
        for (int i = 0; i < length; i++)
        {
            for (int j = 0; j < breadth; j++)
            {
                int minimum = min(y_skyline[i], x_skyline[j]);
                sum += minimum - grid[i][j];
            }
        }

        return sum;
    }
};