class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        new=[]
        while i < len(s):
            if(i+2<len(s) and s[i+2]=="#"):
                new.append(chr(96 + int(s[i]+s[i+1])))
                i+=3
            else:
                new.append(chr(96 + int(s[i])))
                i+=1



        new="".join(new)
        return new



