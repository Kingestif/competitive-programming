# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Core: do inorder traversal, you will have counter that counter whenever you go deep
        ls = [] ; map = defaultdict(list) ; counter = 0
        def func(root,counter):
            if not root:
                return 

            print(root.val)
            map[counter].append(root.val)
            func(root.left,counter + 1)
            func(root.right,counter + 1)

        func(root,counter)
        print(map)
        for key,values in map.items():
            if key % 2 != 0:
                ls.append(values[::-1])
            else:
                ls.append(values)
        return ls


