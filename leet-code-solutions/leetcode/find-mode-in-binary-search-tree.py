# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.map=defaultdict(int)
        self.rep(root)
        print(self.map)
        val = max(self.map.values())
        ls=[]
        for key, value in self.map.items():
            if value == val:
                ls.append(key)
        return ls

    def rep(self,current):
        if not current:
            return None

        self.map[current.val] += 1
        self.rep(current.left)
        self.rep(current.right)

        return self.map


            
        
