class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix=[]    
        for i in range(len(rowSum)):
            new=[]
            for j in range(len(colSum)):
                diff = min(rowSum[i],colSum[j])
                new.append(diff)
                rowSum[i] -= diff
                colSum[j] -= diff
            matrix.append(new)
        # else:
        #     for i in range(len(colSum)):
        #         new=[]
        #         for j in range(len(rowSum)):
        #             diff = min(rowSum[j],colSum[i])
        #             new.append(diff)
        #             rowSum[j] -= diff
        #             colSum[i] -= diff
        #         matrix.append(new)
        return matrix
                    
