class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        start = 0

        if m*n != len(original):
            return []

        for i in range(m):
            ls = []
            for j in range(n):
                ls.append(original[start])
                start += 1
            arr.append(ls)

        return arr
