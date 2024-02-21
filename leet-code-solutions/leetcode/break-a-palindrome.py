class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # check=False
        if len(palindrome) <= 1:
            return ""

        # s=""
        # for i in range(len(palindrome)):
        #     if palindrome[i] != "a" and not check:
        #         s += "a"
        #         check=True
        #     else:
        #         if not check and i==len(palindrome) -1:
        #             s += "b"
        #             print("yes")
        #             break
        #         s += palindrome[i]
        # return s  
        palindrome=list(palindrome)         
        for i in range(len(palindrome)//2):
            if palindrome[i] != "a":
                palindrome[i] = "a"
                return "".join(palindrome)
        palindrome[-1] ="b"
        return "".join(palindrome)

            

        