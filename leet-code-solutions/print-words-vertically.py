class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        print(s)


        # to get the largest length mx
        mx=float('-inf')
        for i in range(len(s)):
            if(len(s[i])>mx):
                mx=len(s[i])
        new=[""]*mx

        # concatenating the items
        for i in range(len(s)):
            for j in range(mx):
                if(j<len(s[i])):
                    new[j]+=s[i][j]
                else:
                    new[j]+=" "
        print(new)

        # Remove the last space from each element in the list using rstrip()
        for i in range(len(new)):
            new[i]=new[i].rstrip()
        return new





