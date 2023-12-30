class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        total=0
        piles.sort(reverse=True)
        n=len(piles)-(len(piles)//3)
        for i in range(n):
            if i%2!=0:
                total+=piles[i]

        return total
        