# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # REFER keven naughton

        # Core: used for future, we gonna start bottom to top instead of top to bottom to hold the nodes of childs with Deleted parents
        # so we traverse using DFS until it becomes null(bottom one) act as base case then we delete that node if its on the "to_delete" then we add its childs to remaining
        remaining = []
        checker = Counter(to_delete)    #for fast checking

        def removeNode(root,remaining):
            if root == None:
                return None

            root.left = removeNode(root.left,remaining)
            root.right = removeNode(root.right,remaining)
            # STAR: the above codes traverse the Tree until its bottom childs become null(last node), next line is where we try to delete 

            # if root needs to be deleted hold on to its left and right childs to "remaining" then make it null by "return None"
            # but if roots not in "to_delete" just "return root"
            if root.val in checker:
                if root.left:
                    remaining.append(root.left)
                if root.right:
                    remaining.append(root.right)
            
            
                return None #after getting hold of its childs delete the node

            return root #if not in checker just return it




        removeNode(root,remaining)

        # Lastly to check the Main root is in checker b/c we get to Main root last b/c its bottom top traversal
        if root.val not in checker:
            remaining.append(root)

        return remaining



    
        
