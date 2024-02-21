from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        total = 0
        map=Counter(answers)
        print(map)
        for key,values in map.items():
            if key == 0:
                total += values
            elif values <= key + 1:
                total += key + 1
            else:
                total += ((values + key) // (key +1)) * (key+1)
        return total

            
