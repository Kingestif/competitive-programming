class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel = 'aeiou'
        vowel = Counter(list(vowel))
        count = 0

        for i in range(left,right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                count += 1

        return count

