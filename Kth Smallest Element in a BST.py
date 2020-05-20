class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        root.arr = []
        if root is not None:   
            self.util(root, root.arr)
        else:
            return
        for i in range(len(root.arr)):
            if i == k-1:
                return root.arr[i]
            
    def util(self,root, arr):
        if root is not None:
            self.util(root.left, arr)
            arr.append(root.val)
            self.util(root.right, arr)  
 
        return