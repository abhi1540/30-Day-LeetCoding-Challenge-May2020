class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        import string

        s1dict = dict.fromkeys(string.ascii_lowercase, 0)
        s2dict = dict.fromkeys(string.ascii_lowercase, 0)
        
        s1len = len(s1)
        s2len = len(s2) 
        print("here")
        if s1len > s2len or s1len == 0 or s2len == 0:
            return False
        print("exit")
        for i in range(s1len):
            if s1[i] in s1dict:
                s1dict[s1[i]] += 1
            else:
                s1dict[s1[i]] = 1
                
        for i in range(s2len-s1len+1):
            
            if i == 0:
                for j in range(i, s1len):
                    if s2[j] in s2dict:
                        s2dict[s2[j]] += 1
                    else:
                        s2dict[s2[j]] = 1
            else:
                s2dict[s2[i-1]] -= 1
                if i+s1len <= s2len:
                    s2dict[s2[i+s1len-1]] += 1
            #print(i,s1dict, s2dict)
            if s1dict == s2dict:
                return True
            else:
                continue
        return False