class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start=0 ; end=0 ; count0=0 ; counter=0
        max=float('-inf')
        while end<len(nums):
            if nums[end]==1:
                counter+=1
                end+=1
            else:
                if count0<k:
                    counter+=1
                    count0+=1
                    end+=1
                
                else:
                    if counter>max:
                        max=counter
                    if nums[start]==0:
                        count0-=1
                    counter-=1
                    start+=1
        if counter>max:
            max=counter
        return max



