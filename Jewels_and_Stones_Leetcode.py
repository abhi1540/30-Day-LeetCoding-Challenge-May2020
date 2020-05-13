class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        
        sdict = {}
        
        res = 0
        
        for i in S:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1
                
        for j in J:
            if j in sdict:
                res += sdict[j]
                
        return res