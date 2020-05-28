class Solution:
    def countBits(self, num: int) -> List[int]:
        
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        if num > 1:
            dp = [0 for i in range(num+1)]
            dp[1] = 1
            
            for i in range(2, num+1):
                if i % 2 == 0:
                    dp[i] = dp[i//2]
                else:
                    dp[i] = dp[i//2] + 1
                    
            return dp