# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ls=[]
        self.func(root)
        return self.ls
        
    def func(self,root):
        if not root:
            return 
        self.ls.append(root.val)
        self.func(root.left)
        self.func(root.right)

    
    