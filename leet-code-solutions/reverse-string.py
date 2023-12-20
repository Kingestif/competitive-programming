class Solution(object):
    def reverseString(self, s):
        i=0
        j=1
        while i<len(s):
            if(i==len(s)//2):
                break
            s[i],s[len(s)-j]=s[len(s)-j],s[i]
            j+=1
            i+=1

        return s


        