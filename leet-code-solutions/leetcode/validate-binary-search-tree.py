# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ls = []
        def func(root):
            # use inorder traversal then if it is sorted it means its definetly BST else its not
            if not root:
                return None

            func(root.left)
            print(root.val)
            ls.append(root.val)
            func(root.right)
           

        func(root)
        print(ls)
        if len(ls) != len(set(ls)):
            return False
        return ls == sorted(ls)