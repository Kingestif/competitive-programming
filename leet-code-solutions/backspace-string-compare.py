class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        snew=[]
        tnew=[]
        def pushx(x):
            if(x!="#"):
                snew.append(x)
            if(x=="#"):
                if(len(snew)!=0):
                    snew.pop()


        def push(y):
            if(y!="#"):
                tnew.append(y)

            if(y=="#"):
                if(len(tnew)!=0):
                    tnew.pop()



        for i in range(len(s)):
            pushx(s[i])

        for i in range(len(t)):
            push(t[i])

        print(snew,tnew)
        snew="".join(snew)
        tnew="".join(tnew)
        return snew==tnew