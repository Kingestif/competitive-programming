class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        maindig={}
        revdig={}

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j not in maindig:
                    maindig[i+j]=mat[i][j]
                else:
                    maindig[i+j]+=mat[i][j]

                if j-i not in revdig:
                    revdig[j-i]=mat[i][j]
                else:
                    revdig[j-i]+=mat[i][j]

        maxi=float('-inf')

        # for i in range(len(mat)):
        #     for j in range(len(mat[i])):
                # sum = maindig[i+j] + revdig[j-i] - mat[i][j]
                # if sum > maxi:
                #     maxi=sum
        if len(mat)%2==0 or len(mat[0])==0:
            sum=revdig[0] + maindig[len(mat[0])-1]
        else:
            sum=revdig[0] + maindig[len(mat[0])-1] - mat[len(mat)//2][len(mat)//2]
        return sum
