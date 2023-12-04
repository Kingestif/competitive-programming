class Solution:
    def largestGoodInteger(self, num: str) -> str:
        map={}
        maxi=float('-inf')
        mvalues=0
        check=False
        for i in range(len(num)):
            if(i+1<len(num)):
                if(num[i]==num[i+1]):
                    if(num[i] not in map):
                        map[num[i]]=0
                    elif(num[i] in map and num[i-1]==num[i]):
                        map[num[i]]+=1

        for key,values in map.items():
            if(values>=1 and int(key)>maxi):
                maxi=int(key)
                mvalues=values
                check=True

        mvalues+=2
        if(check==True):
            return str(maxi)*3
        else:
            return ""


