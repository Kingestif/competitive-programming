class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new=[]
        total=1
        ztotal=1
        counter=0

        for i in range(0,len(nums)):
            total=total*nums[i]
            if(nums[i]!=0):
                ztotal=ztotal*nums[i]
            else:
                counter+=1

        print(total,ztotal)

        for i in range(0,len(nums)):
            if(total==0 and nums[i]!=0):
                nums[i]=0
            elif(total==0 and nums[i]==0):
                if(counter>1):
                    nums[i]=0
                else:
                    nums[i]=ztotal
            else:
                nums[i]=total//nums[i]

        return nums