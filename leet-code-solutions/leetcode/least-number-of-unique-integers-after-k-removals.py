from collections import defaultdict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic=defaultdict(int)
        for i in arr:
            dic[i] += 1
        smap = sorted(dic.items(), key=lambda x: x[1])
        smap = {key: value for key, value in sorted(dic.items(), key=lambda x: x[1])}
        print(smap)
        smap2=smap.copy()

        for key, value in smap2.items():
            if k < value:
                break
            elif k == value:
                del smap[key]
                break

            smap[key] -= k
            k -= value
            if smap[key] <= 0:
                del smap[key]
        return len(smap)