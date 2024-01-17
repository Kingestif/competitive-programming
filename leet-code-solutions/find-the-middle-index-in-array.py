class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # ltotal=nums[0] ; rtotal=nums[-1]
        # start=1 ; end=len(nums)-2
        # while start<len(nums):
        #     print(ltotal,rtotal)
        #     if ltotal==0 and start==len(nums)-1:
        #         return len(nums)-1
        #     if ltotal==rtotal:
        #         return start-1
        #     elif(ltotal<rtotal):
        #         ltotal+=nums[start]
        #         start+=1
        #     else:
        #         rtotal+=nums[end]
        #         end-=1
        # print(ltotal,rtotal)
        
        # return -1

        # prefix sum==suffix sum
        # left=[]
        # total=0
        # for i in range(len(nums)):
        #     total+=nums[i]
        #     left.append(total)

        # total=0 ; right=[]
        # for i in range(len(nums)-1,-1,-1):
        #     total+=nums[i]
        #     right.append(total)

        # print(left,right)
        
        # # two pointer
        # l=0 ; r=0
        # while l<len(nums)-1:
        #     if left[l]==right[r]:
        #         return l
        #     elif left[l]<right[r]:
        #         l+=1
        #     else:
        #         r+=1
        # return -1
        # easy approach

        total=0 
        for i in range(len(nums)):
            total+=nums[i]
            nums[i]=total
        print(nums)

        last=nums[-1]
        for i in range(len(nums)):
            if i==0:
                if last-nums[i]==0:
                    return 0
            elif i==len(nums)-1:
                if nums[i-1]==0:
                    return len(nums)-1
            elif last-nums[i] == nums[i-1]:
                return i
        return -1


        return 23
        




