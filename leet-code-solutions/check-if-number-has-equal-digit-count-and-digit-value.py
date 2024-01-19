class Solution:
    def digitCount(self, num: str) -> bool:
        num=list(num)
        for i in range(len(num)):
            if num.count(str(i))!=int(num[i]):
                return False
        return True
                