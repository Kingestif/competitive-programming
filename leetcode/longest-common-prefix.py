class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x), reverse=True)
        new=""
        check=True
        x=0
        for i in range(len(strs[0])):
            if(check==False):
                break
            for j in range(1,len(strs)):
                if(i>=len(strs[j])):
                    check=False
                    break
                else:
                    if(strs[j][i]!=strs[0][x]):
                        check=False
                        break

            if(check==True):
                new+=strs[0][x]
                x+=1
        return new

