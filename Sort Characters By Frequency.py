class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        dict1 = {}
        
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        st = ""
        list1 = sorted(dict1.items(), key = lambda x: x[1], reverse=True)
        
        for i in list1:
            st += i[0]*i[1]
        
        return st