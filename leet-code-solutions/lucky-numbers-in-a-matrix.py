class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        x = defaultdict(int)
        ans = []
        if len(matrix[0]) == 1:
            return max(matrix)
        for i in range(len(matrix)):
            x[i] = min(matrix[i])

        col = defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                col[j].append(matrix[i][j])

        for j in range(len(matrix[0])):
            col[j] = max(col[j])
        print(x,col)

        for i in range(len(matrix[0])):
            if x[i] in col.values():
                ans.append(x[i])
      

        return ans

