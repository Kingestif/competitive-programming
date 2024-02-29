# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root,p,q):
            if not root:
                return None
                
            elif p.val < root.val and q.val < root.val:
                return func(root.left,p,q)
            elif p.val > root.val and q.val > root.val:
                return func(root.right,p,q)

            return root

        return func(root,p,q)

            

            

            
       
       
       
       
       
       
       
       
        # # base case
        # if not root:
        #     return None
        # elif not root.left and not root.right:
        #     return None

        # if not root.left:
        #     if root.right== p or root.right == q:
        #         return root.right

        # elif not root.right:
        #     if root.left == p or root.left== q:
        #         return root.left

        # else:
        #     if root.left in [p,q] and root.right in [p,q]:
        #         return root


        # return self.lowestCommonAncestor(root.left,p,q) and self.lowestCommonAncestor(root.right,p,q)
