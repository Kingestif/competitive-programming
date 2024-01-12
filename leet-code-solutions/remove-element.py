class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new=nums.copy()
        counter=0
        # for i in range(len(nums)):
        #     if nums[i]!=val and nums[i]!='_':
        #         counter+=1
        #     else:
        #         nums.pop(i)
        #         nums.append('_')
        # print(nums)
        # return counter
        i=0
        while i<len(nums):
            if nums[i]=="_":
                break
            if nums[i]!=val:
                counter+=1
                i+=1
            else:
                nums.pop(i)
                nums.append("_")
        print(counter)
        print(nums)
        return counter
        