# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        def func(root1,root2):
            if not root1 and not root2:
                return None
            if not root1:
                return root2
            elif not root2:
                return root1

                         
            root1.val += root2.val
            root1.left = func(root1.left,root2.left)  
            root1.right = func(root1.right,root2.right)  
            return root1

        return func(root1,root2)
   
   
   
    #     self.tree = TreeNode()
    #     self.func(self.tree,root1,root2)
    #     return self.tree
    # def func(self, tree, root1, root2):
    #     if not root1 and not root2:
    #         return None

    #     if not root1:
    #         self.insert(tree,root2.val)
    #         return
    #     elif not root2:
    #         self.insert(tree,root1.val)
    #         return
    #     else:
    #         self.insert(tree,root1.val + root2.val)

    #     self.func(tree,root1.left,root2.left)
    #     self.func(tree,root1.right,root2.right)
    
    #     return tree

    # def insert(self,current,val):
    #     if val < current.val:
    #         if not current.left:
    #             current.left = TreeNode(val)
    #             return 
    #         self.insert(current.left,val)

    #     else:
    #         if not current.right:
    #             current.right = TreeNode(val)
    #             return 
    #         self.insert(current.right,val)

    #     return current

