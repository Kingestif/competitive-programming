class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mat2=matrix.copy()
        new=[]
        ans=[]
        for i in range(len(mat2[0])):
            new=[]
            for j in range(len(mat2)):
                new.append(mat2[j][i])
            matrix[i]=new[::-1]



            
        