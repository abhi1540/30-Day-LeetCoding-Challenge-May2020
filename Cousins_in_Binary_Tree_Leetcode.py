# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        if root is None:
            return 
        
        root_x, root_y = 0, 0
        depth_x, depth_y = 0, 0
        dict1 = {}
        
        root.height = 0
        
        arr = [(None,root)]
        while len(arr) > 0:
            item = arr.pop(0)
            
            if item[1].height in dict1:
                dict1[item[1].height].append((item[0], item[1].val))
            else:
                dict1[item[1].height] = [(item[0], item[1].val)]
                
            if item[1].left is not None:
                
                item[1].left.height = item[1].height + 1
                arr.append((item[1], item[1].left))
                
            if item[1].right is not None:
                
                item[1].right.height = item[1].height + 1
                arr.append((item[1], item[1].right))
                
        for i,j in dict1.items():
            for k in j:
                
                if k[1] == x:
                    root_x = k[0]
                    depth_x = i
                if k[1] == y:
                    root_y = k[0]
                    depth_y = i
                
                    
        if root_x != root_y and depth_x == depth_y:
            return True
        return False