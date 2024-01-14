class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort() ; odd=[] ; even=[] ; ans=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(odd)):
            ans.append(odd[i])
            ans.append(even[i])
        return ans
            