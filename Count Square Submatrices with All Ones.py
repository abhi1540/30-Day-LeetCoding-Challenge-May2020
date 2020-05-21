    def countSquares(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        mat = [[0 for i in range(cols+1)] for j in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                mat[i+1][j+1] = matrix[i][j] 

        
        for i in range(rows+1):
            for j in range(cols+1):
                if mat[i][j] == 1:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
                    res += mat[i][j]
        
        return res