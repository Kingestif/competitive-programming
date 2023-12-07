class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new=[" "]
        check0=False

        if(0 in spaces):
            check0=True
            spaces.remove(0)

        x=0
        s=list(s)
        for i in range(len(s)):
            if(x<len(spaces) and i==spaces[x]-1):
                s[i]+=" "
                x+=1

        s="".join(s)

        if(check0):
            n=" "
            for i in range(len(s)):
                n+=s[i]
            return n


        else:
           return s

