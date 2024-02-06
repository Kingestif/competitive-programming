class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=strs.copy()
        ss=s.copy()
        x=len(s)

        for i in range(0,x):
            s[i]=list(s[i])
            s[i].sort()
            s[i]="".join(s[i])
        new=[]

        k=0
        for i in range(0,x):
            if(s[i] not in new and s[i]!="0"):
                new.append([ss[i]])
                for j in range(0,x):
                    if(s[i]==s[j] and i!=j):
                        new[k].append(ss[j])
                        s[j]="0"
                k+=1


        return new