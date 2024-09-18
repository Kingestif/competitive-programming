class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # it needs some kind of sorting first
        for i in range(len(nums)):
            for j in range(len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]

        s=""
        for i in nums:
            s+=str(i)

            
        if s[0]=="0":
            return "0"
        else:
            return s






        return 0
        # total=str(nums[0])
        # for i in range(1,len(nums)):
        #     if total + str(nums[i]) > str(nums[i]) + total:
        #         total=total + str(nums[i])
        #     else:
        #         total= str(nums[i]) + total

        
        # return total















        