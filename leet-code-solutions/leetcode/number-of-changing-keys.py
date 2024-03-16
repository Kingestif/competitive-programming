class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        prev = s[0]
        counter = 0
        for i in s[1:]:
            if i != prev:
                counter += 1
                prev = i

        return counter