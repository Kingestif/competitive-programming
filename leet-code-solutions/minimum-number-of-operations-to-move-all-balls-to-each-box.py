class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        new=[]
        for i in range(len(boxes)):
            total=0
            for j in range(len(boxes)):
                if(boxes[j]=='1'):
                    total+=abs(i-j)
            new.append(total)

        return new
        