class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            j1 = 0 ; j2 = len(matrix[0]) - 1 
            start = [i,j1] ; end = [i,j2]
            while start[1] <= end[1] and start[1] < len(matrix[0]):
                mid = (start[1] + end[1]) // 2
                val = matrix[i][mid]
                
                if val > target:    
                    end[1] = mid - 1
                elif val < target:
                    start[1] = mid + 1
                else:
                    print(i,mid)
                    return True
        return False                                                                                                                                                                                                            
           