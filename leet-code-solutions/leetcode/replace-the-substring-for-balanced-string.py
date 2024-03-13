from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        left = 0 ; right = 0    ; target = len(s) // 4
        map = defaultdict(int)
        for i in range(len(s)):
            map[s[i]] += 1

        ans = len(s)
        for right in range(len(s)):
            map[s[right]] -= 1
            while all(map[char] <= target for char in ["Q","W","E","R"]) and left < len(s):
                map[s[left]] += 1
                ans = min(ans,right - left + 1)
                left += 1
        return ans



                

        return 0





        
                


        