class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        index = len(num)
        for i in range(len(num)-1,-1,-1):
            if num[i] != "0":
                break
            index = i

        return num[0:index]

