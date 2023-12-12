class Solution:
    def reverseWords(self, s: str) -> str:
        new=s.split()
        new.reverse()
        st=" ".join(new)
        return st