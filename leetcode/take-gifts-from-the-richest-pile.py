class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        x = 0
        for i in range(k):
            val  = max(gifts)
            x += val
            index = gifts.index(val)
            gifts[index] = math.floor(sqrt(val))

        return sum(gifts)





