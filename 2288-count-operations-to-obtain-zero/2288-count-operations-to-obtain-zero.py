class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        result = 0
        if num1 == 0 or num2 == 0:
            return result
        
        while num1 > 1 and num2 > 1:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            result +=1 

        if num1 == 0 or num2 == 0:
            return result
        
        return result + max(num1, num2)