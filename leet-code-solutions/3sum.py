class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new=[]
        nums.sort()
        print(nums)
        target=0

        for i in range(0,len(nums)-2):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if(sum==target):
                    # print(i,start,end)
                    if([nums[i],nums[start],nums[end]] not in new):
                        new.append([nums[i],nums[start],nums[end]])

                    start+=1
                    end-=1
                elif(sum<target):
                    start+=1
                else:
                    end-=1

        return new