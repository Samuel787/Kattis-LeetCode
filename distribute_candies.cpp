class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> results(num_people, 0);
        int candy = 1;
        int person = 0;
        while(candies > 0){
            if(candy <= candies){
                results[person % num_people] += candy;
                candies -= candy;
            } else {
                results[person % num_people] += candies;
                candies = 0;
            }
            candy++;
            person++;
        }
        return results;
    }
};