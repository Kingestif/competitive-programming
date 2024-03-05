class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[] ; map={}
        def backtrack(perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return

            for i in nums:
                if i not in perm:
                    perm.append(i)
                    backtrack(perm)
                    perm.pop()


                    

            

        backtrack([])
        return ans

        