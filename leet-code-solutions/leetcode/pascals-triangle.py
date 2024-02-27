class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]

        base = [1,1]
        arr=[[1],[1,1]]
        counter = 2
        for i in range(numRows-2):
            new=[]
            print(base)
            for j in range(len(base)):
                if j == len(base) - 1:
                    new.append(base[j])
                elif j == 0:
                    # print(base)
                    new.append(base[j])
                    new.append(base[j] + base[j+1])
                else:
                    new.append(base[j] + base[j+1])
            base = new.copy()
            arr.append(new)
        return arr        


