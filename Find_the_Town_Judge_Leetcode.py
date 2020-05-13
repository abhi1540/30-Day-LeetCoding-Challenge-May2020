class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        dict1 = {}
        for i in trust:
            if i[0] in dict1:
                dict1[i[0]].append(i[1])
            else:
                dict1[i[0]] = [i[1]]
        num = -1
        for i in range(1,N+1):
            if i not in dict1:
                num = i
        for i, j in dict1.items():
            if num not in j:
                return -1
        return num