import numpy as np
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        final=[]
        for column in zip(*strs):
            s=""
            for element in column:
               s+=element
            final.append(s)

        print(final)
        counter=0
        for i in range(len(final)):
            for j in range(1,len(final[i])):
                if ord(final[i][j]) < ord(final[i][j-1]):
                    counter+=1
                    break
        return counter


            

            