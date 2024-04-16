# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        map = defaultdict(list)
        visited = defaultdict(int)

        queue = deque([root])

        # 1st, bidirectionaly adjacency list
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node and node.left:
                    map[node.val].append(node.left.val)
                    map[node.left.val].append(node.val)
                    queue.append(node.left)

                if node and node.right:
                    map[node.val].append(node.right.val)
                    map[node.right.val].append(node.val)
                    queue.append(node.right)

        ans = []
        def DFS(node,counter):
            neighbour = map[node]
            if counter == k and node not in visited:
                ans.append(node)

            visited[node] = 1
            for i in neighbour:
                if i not in visited:
                    DFS(i,counter + 1)

        DFS(target.val,0)
        
        return ans
        











                




         

                
