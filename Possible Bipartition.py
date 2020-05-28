class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        if len(dislikes) == 0 or len(dislikes) == 1 or N == 1:
            return True
        
        """For creating the dictionary"""
        dict1 = {}
        for i in dislikes:
            if i[0] in dict1:
                dict1[i[0]].append(i[1])
            if i[1] in dict1:
                dict1[i[1]].append(i[0])
            if i[0] not in dict1:
                dict1[i[0]] = [i[1]]
            if i[1] not in dict1:
                dict1[i[1]] = [i[0]]
        
        """using Dynamic Programming to keep track of color"""
        dp = [0 for j in range(N+1)]

        queue = []
        """this for loop is to check for disconnected component"""
        for j in range(1,N+1):
            if dp[j] == 0 and j in dict1:
                queue.append(j)
            """this is the main loop to assign color and check if collision"""
            while len(queue) > 0:
                item = queue[0]

                del queue[0]
                """get current color of first queue item and update DP list and append
                neighbours of the first queue item"""
                curr_col = dp[item]

                for i in dict1[item]:  

                    if dp[i] == 0 and curr_col == 1:
                        dp[i] = 2
                        queue.append(i)
                    elif dp[i] == 0 and curr_col == 2:
                        dp[i] = 1
                        queue.append(i)
                    elif dp[i] == 0 and curr_col == 0:
                        dp[i] = 1
                        queue.append(i)        
                    elif dp[i] == curr_col:
                        """if any collision of color of current and its neighbour then return False"""
                        return False
        return True  