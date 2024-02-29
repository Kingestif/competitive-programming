# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls=[]
        def func(root):
            if not root:
                return False

            func(root.left)
            ls.append(root.val)
            func(root.right)
            return 
        
        func(root)
        return ls[k-1]
            
