class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ls = []
        num = ''
        for i in s:
            num += str(ord(i) - ord('a') + 1)

        while k > 0:
            val = list(map(int,num))
            summ = sum(val)
            num = str(summ)
            k -= 1

        return int(num)
        