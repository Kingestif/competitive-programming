class Solution:
    def numberOfWays(self, s: str) -> int:
        counter=0 ; pre0=[] ; total=0 ; pre1=[]
        if len(s) < 3:
            return 0
        for i in s:
            total += int(i)
            pre0.append(total)

        total=0
        for i in s:
            if i=="0":
                total += 1
            pre1.append(total)

        # for 0 
        for i in range(1,len(s)-1):
            if s[i] == "0":
                counter += pre0[i] * (pre0[-1] - pre0[i])

        # for 1
        for i in range(1,len(s)-1):
            if s[i]=="1":
                counter += pre1[i] * (pre1[-1] - pre1[i])

        return counter
