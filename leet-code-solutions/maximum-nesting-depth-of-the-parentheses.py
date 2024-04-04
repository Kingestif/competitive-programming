class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0 ; maxx = float('-inf')
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
                maxx = max(maxx,counter)
            elif s[i] == ")":
                counter -= 1
            
        if maxx == float('-inf'):
            return 0
        return maxx