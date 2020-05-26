class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        sum1 = 0
        arr_len = 0
        lenarr = 0
        dict1 = {0: -1}
        
        for i,j in enumerate(nums):
            if j == 0:
                sum1 -= 1
            else:
                sum1 += 1
            if sum1 in dict1:
                lenarr = i - dict1[sum1]
            else:
                dict1[sum1] = i
            if lenarr > arr_len:
                arr_len = lenarr
        return arr_len