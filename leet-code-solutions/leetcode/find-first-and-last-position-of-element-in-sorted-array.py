class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # each mid must be calculated individually
        # Core:Find the first occurence of the e/t 
        max=0 ; min=0 ; start=0 ; counter = 0 ;check=False
        end=len(nums)-1 ; mid=(start+end)//2
        
        while(start<=end):
            if(target==nums[mid]):
                check=True
                min=mid
                if(mid!=0 and nums[mid-1]==target):    #to find first occurence
                    mid-=1
                else:
                    while(mid!=len(nums)-1 and nums[mid+1]==target):
                        counter+=1
                        mid+=1
                    break
            elif(target > nums[mid]):
                start+=1
                mid=(start+end)//2
            elif(target < nums[mid]):
                end-=1
                mid=(start+end)//2
        new=[]
        max=min+counter

        if check:
            return [min,max]
        else:
            return [-1,-1]
        





