    def findAnagrams(self, s: str, p: str) -> List[int]:
        import string
        list1 = []
        pdict = dict.fromkeys(string.ascii_lowercase, 0)
        sdict = dict.fromkeys(string.ascii_lowercase, 0)
        slen = len(s)
        plen = len(p) 
        
        if slen < plen:
            return list1
        left, right = 0, 0
        
        while right < plen:
            if p[right] in pdict:
                pdict[p[right]] += 1
            else:
                pdict[p[right]] = 1
            if s[right] in sdict:
                sdict[s[right]] += 1
            else:
                sdict[s[right]] = 1
            right += 1

        right -= 1    
        while right < slen:
            if pdict == sdict:
                list1.append(left)
            right += 1 
            if right != slen:
                if s[right] in sdict:
                    sdict[s[right]] += 1
                else:
                    sdict[s[right]] = 1
            sdict[s[left]] -= 1
            left += 1
            #print(sdict,pdict)
            
        return list1