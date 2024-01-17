class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        start=0 ; end=0 ; value=0
        new=[0]*len(s)
        for i in range(len(shifts)):
            start=shifts[i][0] ; end=shifts[i][1] ; value=shifts[i][2]
            if value==0:
                new[start]+=-1
            else:
                new[start]+=1

            if end+1<len(s):
                if value==1:
                    new[end+1]+=-1
                else:
                    new[end+1]+=1


        total=0 
        print(new)

        for i in range(len(new)):
            total+=new[i]
            new[i]=total


        print(new)
        ans=""
        for i in range(len(s)):
            if new[i] == 0:
                ans += s[i]
            else:
                shifted_code = (ord(s[i]) - 97 + new[i]) % 26
                ans += chr(shifted_code + 97)

        return ans




            

        # for adding 123%122 if < 97: +96
        # for subtruct if 97-(ord-num)>0 123- (97-(ord-num))
        return "gd"