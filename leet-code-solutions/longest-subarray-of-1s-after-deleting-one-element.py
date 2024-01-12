class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # new=[] ; counter=0
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         counter+=1
        #         if i==len(nums)-1:
        #             new.append(counter)
                    
        #     else:
        #         if i==len(nums)-1:
        #             new.append(counter)
        #             break
        #         if nums[i+1]!=0:
        #             new.append(counter)

        #         counter=0
        # print(new)
        # new.sort(reverse=True)
        # if len(new)==1:
        #     if new[0]!=0:
        #         return new[0]-1
        #     else:
        #         return 0
        # else:
        #     return new[0]+new[1]
        if sum(nums)==len(nums):
            return len(nums)-1
        count1=0
        count0=0
        start=0 ; end=0 ; max=float('-inf')
        while end<len(nums):
            if count0<2:
                if nums[end]==1:
                    count1+=1
                else:
                    count0+=1

                end+=1
                if end==len(nums):
                    if count1>max:
                        max=count1
                    break
            else:
                if count1>max:
                    max=count1

                if nums[start]==0:
                    count0-=1
                else:
                    count1-=1
                start+=1
               
        return max
        