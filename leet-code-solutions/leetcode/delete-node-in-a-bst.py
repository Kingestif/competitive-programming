# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # self.getMin(root)
        
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.right:
                root = root.left    #this also the below way both works
            elif not root.left:
                return root.right
            else:   #2 childs
                temp = self.getMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
                return root

        return root

    def getMin(self,root):
        current = root
        while current.left:
            current = current.left
        return current

        

        
            
            




