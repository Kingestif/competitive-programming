from collections import defaultdict
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        map=Counter(s)
        odd=False
        total=0
        for key,values in sorted(map.items(),reverse=True):
            if values % 2 == 0:
                total += values
            else:
                if not odd:
                    total += values
                    odd=True
                else:
                    total += values - 1
        return total 
