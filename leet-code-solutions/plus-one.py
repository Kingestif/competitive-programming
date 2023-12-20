class Solution(object):
    def plusOne(self, digits):
        x=len(digits)-1
        i=0
        total=0

        while(x>=0):
            total+=digits[i]*(10**x)
            x-=1
            i+=1

        add=str(total+1)
        arr2=[None]*len(add)

        for i in range(0,len(add)):
            arr2[i]=int(add[i])

        return arr2






        