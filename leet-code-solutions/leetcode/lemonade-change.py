from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map=defaultdict(int)
        for i in bills:
            if i == 5:
                map[5] += 1

            if i == 10:
                if map[5] < 1:
                    return False
                else:
                    map[5] -= 1
                    map[10] += 1
            elif i == 20:
                # if map[5] < 1 or map[10] < 1:
                #     return False
                if map[5] < 1:
                    return False
                elif map[10] < 1:
                    if 5 * map[5] < 15:
                        return False
                    else:
                        map[5] -= 3
                    map[20] += 1

                else:
                    map[5] -= 1
                    map[10] -= 1

                    if map[5] < 0:
                        map[5] = 0
                    elif map[10] < 0:
                        map[10] = 0
        return True           


