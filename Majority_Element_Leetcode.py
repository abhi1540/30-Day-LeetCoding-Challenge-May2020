class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict1 = {}
        
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        for i,j in enumerate(dict1):
            if j in dict1:
                if dict1[j] >= len(nums) / 2:
                    return j
                