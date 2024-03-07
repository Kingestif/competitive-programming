from collections import defaultdict
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        map  = defaultdict(int)
        for i in range(len(arr)):
            map[i] = abs(arr[i] - x)

        sormap = dict(sorted(map.items(), key=lambda item: item[1]))

        print(map)
        print(sormap)
        num = []
        counter = 0
        for key,values in sormap.items():
            if counter < k:
                num.append(arr[key])
            else:
                break
            counter += 1

        return sorted(num)

