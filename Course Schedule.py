class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        dict1 = {}
        for i in prerequisites:
            if i[0] not in dict1:
                dict1[i[0]] = [i[1]]
            else:
                dict1[i[0]].append(i[1])
 

        indegree = [0 for j in range(numCourses)]

        for i, j in prerequisites:
            indegree[j] += 1
            
        stack = []
        for i in range(numCourses):
            if indegree[i] == 0:
                stack.append(i)
                
        #print(indegree, stack)
        count = 0
        while len(stack) > 0:
            #print(stack)
            item = stack.pop()
            count += 1
            if item in dict1:
                for i in dict1[item]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        stack.append(i)

                    
        return count == numCourses