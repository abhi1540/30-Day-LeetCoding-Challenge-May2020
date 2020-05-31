class Solution:
    
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
       
        dict1 = {}
        for i in points:
            dict1[tuple(i)] = self.util(i)
            
        list1 = sorted(dict1.items(), key=lambda x: x[1])[:K]
        
        return [i[0] for i in list1]
              
        
    def util(self, point):
        
        return point[0]**2 + point[1]**2
