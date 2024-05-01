class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        if x == -1:
            return word

        ans = list(word[:x+1])
        ans.reverse()
        return "".join(ans) + word[x+1:]

