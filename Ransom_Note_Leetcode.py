class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dict1 = {}
        if len(ransomNote) != "" or len(magazine) != "":
            
            for i in magazine:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1


            for j in ransomNote:
                if j in dict1:
                    dict1[j] -= 1
                else:
                    return False

            for i,j in dict1.items():
                if j < 0:
                    return False

        return True