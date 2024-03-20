from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []
        # sort based on values
        new = dict(sorted(count.items(),key = lambda item: item[1], reverse = True))
        print(new)
        for key,values in new.items():
            if k > 0:
                k -= 1
                ans.append(key)
        return ans
        