class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        s=" ".join(words)
        x=s[::-1]
        x=x.split()
        x.reverse()

        for i in range(len(words)):
            if words[i] == x[i]:
                return words[i]

        return ""


        