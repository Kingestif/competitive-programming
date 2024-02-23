class Solution:
    def minFlips(self, target: str) -> int:
        prev="0"
        counter=0
        for i in range(len(target)):
            if target[i] != prev:
                counter += 1
                if prev=="0":
                    prev="1"
                else:
                    prev="0"
        return counter
