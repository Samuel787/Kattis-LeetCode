

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.window = []
        for num in nums:
            self.binaryInsert(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.binaryInsert(val)
        return self.window[0]

    def binaryInsert(self, num):
        if len(self.window) == 0:
            self.window.append(num)
        elif num <= self.window[0]:
            self.window.insert(0, num)
        elif num > self.window[-1]:
            self.window.append(num)
        else:
            # Assert num belongs in index 0 and N exclusive
            left = 0
            right = len(self.window) - 1
            while left <= right:
                mid = (left + right) // 2
                # print("this is the window: " + str(self.window) + ' and this is the mid: ' + str(mid))
                if self.window[mid] <= num and self.window[mid + 1] >= num:
                    self.window.insert(mid + 1, num)
                    break
                elif self.window[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1

        while len(self.window) > self.k:
            self.window.pop(0)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)