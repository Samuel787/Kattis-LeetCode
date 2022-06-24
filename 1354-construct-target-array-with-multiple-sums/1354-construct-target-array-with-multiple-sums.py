class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        curr_sum = 0
        curr_max = 0
        curr_max_idx = 0
        count = 0
        for i in target:
            curr_sum += i
            if i > curr_max:
                curr_max = i
                curr_max_idx = count
            count += 1
        diff = curr_sum - curr_max
        if curr_max == 1 or diff == 1:
            return True
        if diff > curr_max or diff == 0 or curr_max % diff == 0:
            return False
        target[curr_max_idx] %= diff
        return self.isPossible(target)
        