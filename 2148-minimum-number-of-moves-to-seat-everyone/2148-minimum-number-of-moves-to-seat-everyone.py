class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        students.sort()
        absDiffSum = 0
        idx = 0
        seats.sort()
        for student in students:
            absDiffSum += abs(student - seats[idx]) 
            idx += 1
        return absDiffSum