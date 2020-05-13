class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        left = 1
        right = n + 1
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):  
                res = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return res
        