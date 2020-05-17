    def findAnagrams(self, s: str, p: str) -> List[int]:
        import string
        list1 = []
        pdict = dict.fromkeys(string.ascii_lowercase, 0)
        sdict = dict.fromkeys(string.ascii_lowercase, 0)
        slen = len(s)
        plen = len(p) 
        
        if slen < plen:
            return list1
        
        for i in range(plen):
            if p[i] in pdict:
                pdict[p[i]] += 1
            else:
                pdict[p[i]] = 1
 
            
        for i in range(slen-plen+1):
            if i == 0:
                for j in range(i,plen):
                    if s[j] in sdict:
                        sdict[s[j]] += 1
                    else:
                        sdict[s[j]] = 1
            else:
                sdict[s[i-1]] -= 1
                if i+plen <= slen:
                    sdict[s[i+plen-1]] += 1
            if pdict == sdict:
                list1.append(i)
        return list1  
