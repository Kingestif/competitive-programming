class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        length=n ; n=str(1) 
        for i in range(length-1):
            s="" ; new=[]
            for i in range(len(n)):
                if i == 0:
                    s+=n[i]
                elif n[i]==n[i-1]:
                    s+=n[i]
                else:
                    new.append(s)
                    s=""
                    s+=n[i]

            if len(s) > 0:
                new.append(s)
            ans=""

            for i in range(len(new)):
                ans+=(str(len(new[i]) )+ new[i][0])
            n=ans
        return ans

        