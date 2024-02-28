# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        self.current = root
        self.insert(self.current, val)
        return root

    def insert(self,current,val):
        # if not current:
        #     current = TreeNode(val)
        #     return current

        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
                return 
            self.insert(current.left,val)
            
        else:
            if not current.right:
                current.right = TreeNode(val)
                return 
            self.insert(current.right,val)
        



        





