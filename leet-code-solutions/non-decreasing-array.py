class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        counter=0
        i=0
        while i < len(nums)-1:
            if nums[i]>nums[i+1]:
                if(i==0):
                    if counter==0:
                        counter+=1
                        nums[i]=min(nums)
                    else:
                        return False
                        break
                else:
                    if counter==0:
                    
                        if i+1 == len(nums)-1: #check if its last item
                            return True
                            break

                        # counter+=1
                        # nums[i]=nums[i-1]

                        else:
                            if nums[i+2]>=nums[i]:
                                counter+=1
                                nums[i+1]=nums[i]
                            else:
                                counter+=1
                                nums[i]=nums[i-1]

                    else:
                        return False
                        break
            else:
                i+=1

        return True

