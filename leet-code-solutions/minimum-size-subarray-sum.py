class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min=float('inf')
        start=0
        end=0
        counter=end-start
        total=0
        while(end<len(nums)):
            total+=nums[end]
            end+=1

            while(total>=target):
                counter=end-start
                total-=nums[start]
                start+=1

                if(counter<min):
                    min=counter

            print(total,min)
        if(min==float('inf')):
            return 0
        else:
            return min