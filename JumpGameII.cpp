class Solution
{
public:
    int jump(vector<int> &nums)
    {
        vector<int> min_steps;
        // trivially the number of steps required by just walking to that index
        for (int i = 0; i < nums.size(); i++)
        {
            min_steps.push_back(i);
        }
        for (int i = 0; i < nums.size(); i++)
        {
            int target;
            int steps;
            // from here, can reach next index
            target = max(i + 1, i + nums[i]);
            if (target >= nums.size())
            {
                target = nums.size() - 1;
            }
            steps = min_steps[i] + 1;
            for (int j = i + 1; j <= target; j++)
            {
                min_steps[j] = min(min_steps[j], steps);
            }
        }
        return min_steps[nums.size() - 1];
    }
};