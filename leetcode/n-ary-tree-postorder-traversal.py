"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ls = []

        def DFS(node):
            if not node:
                return 
            
            for child in node.children:
                DFS(child)

            ls.append(node.val)     #after visiting all its children, current node is inserted

        DFS(root)

        return ls



        


