class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = []   ;   right = []
        l = 0   ;   r = len(text) - 1
        count = 0
        while l < len(text):
            left.append(text[l])
            right.append(text[r])

            rev = right[::-1]
            if left == rev:
                count += 2
                left = [] ;  right = []
                
            l += 1  ;   r -= 1

        return count //2
        




