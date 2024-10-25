class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        imap = set()
        jmap = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    imap.add(i)
                    jmap.add(j)


        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in imap or j in jmap:
                    matrix[i][j] = 0

        
