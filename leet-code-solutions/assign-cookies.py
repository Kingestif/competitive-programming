class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()    ; s.sort() ; counter=0
        # check=g.copy()
        # if len(s)==0:
        #     return 0
        # for i in range(len(g)):
        #     if g[i] > max(s):
        #         break
        #     for j in range(len(s)):
        #         if g[i] <= s[j]:
        #             print(g[i],s[i])
        #             counter+=1
        #             s[j]=float('-inf')
        #             break
        # return counter

        # Two pointer
        left=0 ; right=0 ; counter=0
        while left<len(g) and right <len(s):
            if g[left] <= s[right]:
                counter+=1
                left+=1 ; right+=1
            else:
                right+=1
        return counter


