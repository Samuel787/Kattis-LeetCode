class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        count = 0
        basketIdx = 0
        for quantity in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= quantity:
                    count += 1
                    baskets[i] = -1
                    break 
        return len(fruits) - count
