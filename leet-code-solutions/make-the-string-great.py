class Solution:
    def makeGood(self, s: str) -> str:
        ans = []

        def push(x):
            if len(ans) == 0:
                ans.append(x)
            elif x == ans[-1]:
                ans.append(x)
            elif x.upper() == ans[-1] or x.lower() == ans[-1]:
                ans.pop()
            else:
                ans.append(x)

        for i in range(len(s)):
            push(s[i])

        return "".join(ans)