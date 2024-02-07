from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        map=defaultdict(int)    ; arr=[]
        start=0 ; end=0 ; max=float('-inf')
        while end < len(fruits):
            if len(map) < 3:
                map[fruits[end]] += 1
                end+=1
            else:
                if end - start - 1 > max:
                    max = end - start - 1

                map[fruits[start]] -= 1
                if map[fruits[start]] <= 0:
                    del map[fruits[start]]
                start += 1
        if len(map) < 3:
            if end - start> max:
                max = end - start
        else:
            if end - start - 1 > max:
                max = end - start - 1
        return max


        