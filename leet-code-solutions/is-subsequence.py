class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using dp, first do using 2 pointer
        def dp(l,r):
            if r >= len(t) or l >= len(s):
                return 0

            if s[l] == t[r]:
                return dp(l+1,r+1) + 1
            else:
                return dp(l,r+1)


        val = dp(0,0)
        return val == len(s)

        