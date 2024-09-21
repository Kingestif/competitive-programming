class Solution:
    def convertDateToBinary(self, date: str) -> str:
        val = date.split('-')
        ans = []
        x = int(val[0])
        y = int(val[1])
        z = int(val[2])
        ans.append(bin(x)[2:])
        ans.append(bin(y)[2:])
        ans.append(bin(z)[2:])

        return '-'.join(ans)
        