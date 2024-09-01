class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        val = bin(n)[2:]
        val = list(val)
        val.reverse()
        print(val)
        even = 0
        odd = 0
        for i in range(len(val)):
            if val[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1

        return [even,odd]

        