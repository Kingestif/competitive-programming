# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        ans = []

        while queue:
            node = queue.popleft()

            if node:
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        
        return len(set(ans)) == 1
                







