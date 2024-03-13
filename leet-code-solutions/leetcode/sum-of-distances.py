from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # LEFT SIDE
        lindex = defaultdict(int)  #as goes through
        count = defaultdict(int)
        total = 0
        ans = []
        for i in range(len(nums)):
            ans.append(count[nums[i]] * i - lindex[nums[i]])
            lindex[nums[i]] += i
            count[nums[i]] += 1

        rindex = defaultdict(int)
        rcount = defaultdict(int)
        rtotal = 0
        rans = []

        # right sum
        for i in range(len(nums)-1 , -1, -1):
            rans.append(rindex[nums[i]] - (rcount[nums[i]] * i))
            rindex[nums[i]] += i
            rcount[nums[i]] += 1

        rans.reverse()
        
        # finally
        for i in range(len(ans)):
            ans[i] += rans[i]

        return ans






        return [0,3]


