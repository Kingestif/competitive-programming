class Solution:
    def isHappy(self, n: int) -> bool:

        s=str(n)
        x=0
        while(x<50):
            total=0
            for i in range(0,len(s)):
                total+=int(s[i])**2

            s=str(total)
            print(s)
            if(s=='1'):
                return True
                break
            x+=1
        return False


