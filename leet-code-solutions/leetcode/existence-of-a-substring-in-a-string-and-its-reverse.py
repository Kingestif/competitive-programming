class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1,len(s)):
            if s[i] + s[i - 1] in s:
                return True
        return False
