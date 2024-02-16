class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left=0 ; right=0    ; new=[]
        while left< len(firstList) and right < len(secondList):
            # if intersection
            if secondList[right][0] <= firstList[left][1] and secondList[right][1] >= firstList[left][0]:
                temp=[]
                temp.append(max(secondList[right][0], firstList[left][0]))
                temp.append(min(secondList[right][1], firstList[left][1]))
                new.append(temp)

            if firstList[left][1] < secondList[right][1]:
                left+=1
            else:
                right+=1
        return new