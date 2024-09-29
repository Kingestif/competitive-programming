class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        lcount = 0
        rcount = 0

        for i in range(len(s)):
            if s[i] == 'R':
                rcount += 1
            else:
                lcount += 1

            if lcount == rcount:
                ans += 1

        return ans
        