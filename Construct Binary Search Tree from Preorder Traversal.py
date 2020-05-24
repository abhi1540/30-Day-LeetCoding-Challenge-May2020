class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = None
        n = len(preorder)
        
        if n > 0:
            i = 0
            root = TreeNode(preorder[0])
            while i < n:
                if preorder[i] > root.val:
                    break
                i += 1
            
            root.left = self.bstFromPreorder(preorder[1:i])
            root.right = self.bstFromPreorder(preorder[i:])

        return root
        