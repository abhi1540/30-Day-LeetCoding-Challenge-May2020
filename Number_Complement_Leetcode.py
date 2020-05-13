class Solution:
    def findComplement(self, num: int) -> int:
        
        count = 0
        res = 0
        for i in reversed(bin(num).replace("0b", "")):
            if i == "0":
                res += (2**count)
                count += 1
            else:
                count += 1
        return res