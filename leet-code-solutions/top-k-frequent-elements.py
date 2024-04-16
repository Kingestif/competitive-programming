from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        map = defaultdict(list)
        ans = []
        # using min heap


        for key,values in count.items():
            map[values].append(key)
            ans.append(values)

        final = nlargest(k,ans)

        finn = []
        for i in final:
            neighbour = map[i]
            for j in neighbour:
                finn.append(j)
            
        return set(finn)









        # for key,values in map.items():
        #     if len(ans) < k:
        #         ans.append(values)
        # heapify(ans)

        # for key,values in map.items():
        #     if k <= 0 and key > ans[0]:
        #         heappop(ans)
        #         heappush(ans,key)
        #     k -= 1
        # final = []


        # print("ans",ans)
        # for i in ans:
        #     x = map[i]
        #     for j in x:
        #         final.append(j)
        # return set(final)







        return [1,2]
        