class Solution:
    def minimumChairs(self, s: str) -> int:
        mx = float('-inf')
        count = 0
        for i in s:
            if i == "E":
                count += 1
                mx = max(mx,count)
            else:
                count -= 1

        return mx