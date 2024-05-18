class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # using 2 pointer
        i = 0   ;   j = 0
        count = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1

        return i == len(s)