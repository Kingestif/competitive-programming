from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        map=defaultdict(int)
        nums.sort()
        prefix=[0] * (len(nums) + 2)
        for row in requests:
            prefix[row[0]] += 1
            prefix[row[1] + 1]  -= 1
        total = 0

        # prefix sum for counting frequency of occurrence of an index
        for i in range(len(prefix)):
            total += prefix[i]
            prefix[i] = total

        print(prefix)

        # key(index) value(frequency) pair
        for i in range(len(prefix)):
            map[i] = prefix[i]

        # sorted of above map
        sormap = dict(sorted(map.items(), key=lambda x: x[1], reverse=True))
        print(sormap)
        val=len(nums)-1

        # make the greatest frequency the last sorted(largest) number
        for key,values in sormap.items():
            sormap[key] = nums[val] * values
            val -= 1
        print(sormap)
        return sum(sormap.values()) % (10**9 + 7)
        # return result % (10**9 + 7)



