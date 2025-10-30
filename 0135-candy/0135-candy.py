class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1 for _ in ratings]

        # left to right
        for i in range(len(ratings)):
            if i == 0:
                continue
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # right to left
        for i in range(len(ratings) - 1, -1, -1):
            if i == len(ratings) - 1:
                continue
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        
        return sum(candies)
