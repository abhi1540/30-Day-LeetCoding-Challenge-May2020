class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dict1 = {}
        
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        for i,j in enumerate(s):
            if dict1[j] == 1:
                return i
        return -1