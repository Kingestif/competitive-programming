class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        start = 0   ; end = 1   ;   maxx = float('-inf')
        prev = word[0]  ; map = defaultdict(int)    ; map[word[0]] += 1
        check = ['a', 'e', 'i', 'o', 'u']   
        while start < end and end < len(word):
            if ord(word[end]) >= ord(prev):  #valid to include that
                map[word[end]] += 1
                prev = word[end]
                end += 1
            else:
                bo = True
                for i in check:
                    if i not in map:
                        bo = False
                        break

                if bo and end - start > maxx:
                    maxx = end - start
                start = end ; prev = word[end] ; end += 1
                map = defaultdict(int)    ;   map[prev] += 1

        bo = True
        for i in check:
            if i not in map:
                bo = False
                break
                
        if bo and end - start > maxx:
            maxx = end - start

        if maxx == float("-inf"):
            return 0
        return maxx







