class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        check=['a','e','i','o','u']
        start=0
        end=0
        vcount=0
        max=float('-inf')

        for i in range(0,len(s)):
            if(end<k):
                if(s[i] in check):
                    vcount+=1
            else:
                if(s[start] in check):
                    vcount-=1
                if(s[i] in check):
                    vcount+=1

                start+=1

            if(vcount>max):
                max=vcount
            end+=1


        return max       