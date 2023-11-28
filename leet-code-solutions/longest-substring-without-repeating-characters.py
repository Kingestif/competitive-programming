class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        new=[]
        start=0
        end=0
        max=float("-inf")
        while end<len(s):
            if(s[end] not in new):
                new.append(s[end])
                end+=1
            else:
                new.pop(0)
                start+=1
            if(end-start>max):
                max=end-start
        return max
