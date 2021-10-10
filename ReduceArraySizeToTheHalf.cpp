class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> count_map;
        for (int i = 0; i < arr.size(); i++) {
            count_map[arr[i]]++;
        }
        vector<int> count_vector;
        for (const auto& [key, value] : count_map) {
            count_vector.push_back(value);
        }
        sort(count_vector.begin(), count_vector.end(), greater<int>());
        int half_size = arr.size() / 2;
        int result = 0;
        for (int i = 0; i < count_vector.size(); i++) {
            half_size -= count_vector[i];
            result++;
            if (half_size <= 0) {
                break;
            }
        }
        return result;
    }
};
