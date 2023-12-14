class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")

        i=0; j=0

        while i<len(version1) or j<len(version2):
            if i<len(version1):
                version1[i]=int(version1[i])
                i+=1
            if j<len(version2):
                version2[j]=int(version2[j])
                j+=1
        print(version1,version2)
        if version1==version2:
            return 0


        if len(version1)>len(version2):
            for i in range(len(version1)):
                if i < len(version2):
                    if version1[i] > version2[i]:
                        return 1
                    elif(version1[i] < version2[i]):
                        return -1
                else:
                    if version1[i]==0 and i==len(version1)-1:
                        return 0
                    elif version1[i]!=0:
                        return 1
        else:
            for i in range(len(version2)):
                if i < len(version1):
                    if version1[i] > version2[i]:
                        return 1
                    elif(version1[i] < version2[i]):
                        return -1
                else:
                    if version2[i]==0 and i==len(version2)-1:
                        return 0
                    if version2[i]!=0 and i==len(version2)-1:
                        return -1


                        
                    



