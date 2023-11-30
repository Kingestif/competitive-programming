class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new=heights.copy()
        heights.sort()
        counter=0
        for i in range(len(heights)):
            if(new[i]!=heights[i]):
                counter+=1
        return counter

