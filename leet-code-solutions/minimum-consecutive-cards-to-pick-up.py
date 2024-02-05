class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        map={}  ; max=float('inf') 
        for i in range(len(cards)):
            if cards[i] not in map:
                map[cards[i]]=i
            else:
                if i - map[cards[i]] + 1 < max:
                    max=i - map[cards[i]] + 1
                map[cards[i]] = i
        if max==float('inf'):
            return -1
        else:
            return max

        