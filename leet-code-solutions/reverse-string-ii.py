class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # splitted=[]
        # var=k*2
        # for i in range(len(s)):
        #     if i==0:
        #         new=s[:var]
        #     else:
        #         new=s[var:var*2]
        #         var=var*2
        #     splitted.append(new)
        # splitted = [element for element in splitted if element.strip()]
        # print(splitted)


        # final=[]
        # for i in range(len(splitted)):
        #     a=""
        #     b=""
        #     for j in range(len(splitted[i])):
        #         if j < k:
        #             a += splitted[i][j]
        #         else:
        #             b += splitted[i][j]
        #     print(a,b)

        #     a=list(a)
        #     a.reverse()
        #     a="".join(a)
        #     a+=b
        #     final.append(a)
        # final="".join(final)
        # return final
        st=""
        reverse=True
        for i in range(0,len(s),k):
            if reverse:
                new=s[i: i + k][::-1]
                st += new
                reverse=False
            else:
                new=s[i: k + i]
                st+=new
                reverse=True

        return st






