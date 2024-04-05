# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            arr = []
            for i in queue:
                if i:
                    arr.append(i.val)
            ans.append(arr)

            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return ans

            


            