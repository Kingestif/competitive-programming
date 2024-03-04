from collections import defaultdict
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [] ; n = len(nums) 
        map = defaultdict(int)
        def backtrack(i,subset,n):
            if tuple(subset[:]) not in map:
                map[tuple(subset[:])] = 1
                ans.append(tuple(subset[:]))

            if i >= n:
                return

            # choose
            subset.append(nums[i])
            backtrack(i+1,subset,n)

            subset.pop()
            backtrack(i+1,subset,n)
            
            return subset
            
        backtrack(0,[],n)
        return ans