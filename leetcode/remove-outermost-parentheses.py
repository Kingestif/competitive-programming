class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        start = 1
        ans = ""

        def stack(i):
            nonlocal ans
            nonlocal start
            if s[i] == '(':
                if start == 0:
                    start += 1
                else:
                    start += 1
                    ans += '('
            
            elif s[i] == ')':
                if start - 1 != 0:
                    start -= 1
                    ans += s[i]
                else:
                    start -= 1

        for i in range(1,len(s)):
            stack(i)

        return ans

