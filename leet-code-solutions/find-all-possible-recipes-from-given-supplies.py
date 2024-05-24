class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        incoming = [0 for i in range(len(recipes))]  
        graph = defaultdict(list) 
        queue = deque()
        order = []

        for row in range(len(ingredients)):
            for j in range(len(ingredients[row])):
                incoming[row] += 1   
                graph[ingredients[row][j]].append(row)  

        
        for i in range(len(recipes)): 
            if incoming[i] == 0:
                queue.append(i)

        for i in supplies:
            queue.append(i)

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()

                neighbour = graph[node]
                for val in neighbour:
                    incoming[val] -= 1

                    if incoming[val] == 0:
                        order.append(recipes[val])
                        queue.append(recipes[val])

        return order