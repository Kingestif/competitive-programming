class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed = Counter(allowed)
        for i in words:
            check = True
            for j in i:
                if j not in allowed:
                    check = False
                    break
            if check:
                count += 1

        return count
