from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0   ; end = 0   ; map=defaultdict(int)
        maxi = float('-inf')
        while start <= end and end < len(s):
            map[s[end]] += 1
            if (end - start + 1) - max(map.values()) <= k:
                maxi = max(maxi, end - start + 1)
                # end += 1
            else:
                map[s[start]] -= 1
                start += 1
            end += 1
        return maxi