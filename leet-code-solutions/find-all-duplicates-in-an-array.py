from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Core: first know what cyclic sort is (it sort e/ts in o(N) that range from [1,N]) so use that concept 
        i = 0   ;   ans = []
        while i < len(nums):
            index = nums[i] - 1
            if nums[i] - i != 1:
                if nums[index] == nums[i]:
                    ans.append(nums[index])
                    i += 1
                else:
                    nums[index], nums[i] = nums[i], nums[index]
            else:
                i += 1
        return set(ans)