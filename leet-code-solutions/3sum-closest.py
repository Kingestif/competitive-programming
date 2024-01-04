class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        new=[]
        nums.sort()
        min=float('inf') ; value=0

        for i in range(0,len(nums)-2):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if(sum==target):
                    # if([nums[i],nums[start],nums[end]] not in new):
                    #     new.append([nums[i],nums[start],nums[end]])
                    return target
                elif(sum<target):
                    if(abs(sum-target)<min):
                        min=abs(sum-target)
                        value=sum
                    start+=1
                else:
                    if(abs(sum-target)<min):
                        min=abs(sum-target)
                        value=sum
                    end-=1

        return value
        