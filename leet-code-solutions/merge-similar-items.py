class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        val = defaultdict(int)
        for x,y in items1:
            val[x] += y

        for x,y in items2:
            val[x] += y

        ans = []
        for key,values in val.items():
            ans.append([key,values])

        ans.sort()
        return ans