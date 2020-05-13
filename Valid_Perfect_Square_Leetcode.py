class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        if num <= 0:
            return False
        
        temp = num // 2
        
        while temp * temp > num:
            
            temp = (temp + num // temp ) // 2
        
        return temp * temp == num