class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        start = 0 ; end = len(s) - 1

        while start < end:
            if s[start] != s[end]:
                s[start] = s[start] if ord(s[start]) < ord(s[end]) else s[end]
                s[end] = s[start]

            start += 1
            end -= 1

        return "".join(s)

        

        

            
