class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        temp = image[sr][sc]
        self.util(image, sr, sc, newColor, rows, cols, temp)
        
        return image

            
            
            
    def util(self, image, sr, sc, newColor, rows, cols, temp):
        
        
        if sr < 0 or sc < 0 or sr >= rows or sc >= cols or image[sr][sc] != temp or image[sr][sc] == newColor:
            return  
        
        #print(sr,sc, temp)
        image[sr][sc] = newColor


        self.util(image, sr-1, sc, newColor, rows, cols, temp)
        self.util(image, sr, sc-1, newColor, rows, cols, temp)
        self.util(image, sr, sc+1, newColor, rows, cols, temp)
        self.util(image, sr+1, sc, newColor, rows, cols, temp)