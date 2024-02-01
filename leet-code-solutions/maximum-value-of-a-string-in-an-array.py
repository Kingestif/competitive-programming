class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max=float("-inf")
        for i in strs:
            try:
                int(i)
                if int(i) > max:
                    max=int(i)
                print(max)
            except ValueError:
                if len(i) > max:
                    max=len(i)
                print(max)
        return max
        