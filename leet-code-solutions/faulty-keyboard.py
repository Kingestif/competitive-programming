class Solution:
    def finalString(self, s: str) -> str:
        string = []
        for i in range(len(s)):
            if s[i] != 'i':
                string.append(s[i])
            else:
                string.reverse()
        return "".join(string)