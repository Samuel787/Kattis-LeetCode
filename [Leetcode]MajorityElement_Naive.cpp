class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        unordered_map<int, int> map;
        int threshold = nums.size() / 2 + 1;
        for (int i = 0; i < nums.size(); i++)
        {
            map[nums[i]] += 1;
            if (map[nums[i]] >= threshold)
            {
                return nums[i];
            }
        }
        return -1;
    }
};