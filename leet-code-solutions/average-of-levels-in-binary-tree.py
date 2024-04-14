# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            summ = 0
            counter = 0

            for i in range(len(queue)):
                node2 = queue.popleft()
                if node2:
                    counter += 1
                    summ += node2.val

                if node2:
                    queue.append(node2.left)
                    queue.append(node2.right)

            if counter > 0:
                ans.append(summ/counter)

        return ans

                
