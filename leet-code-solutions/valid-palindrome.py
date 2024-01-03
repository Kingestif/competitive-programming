import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumerics = string.ascii_letters + string.digits
        ss=""
        for i in s:
            if i in alphanumerics:
                ss+=i

        ss=ss.lower()
        print(ss)

        start=0
        end=len(ss)-1

        while start<end:
            if ss[start]!=ss[end]:
                return False
            start+=1 ; end-=1
        return True


        return 0

        