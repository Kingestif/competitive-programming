class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter=0
        max=counter
        for i in range(0,len(nums)):
            if(nums[i]==1):
                counter+=1
            else:
                if(counter>max):
                    max=counter
                counter=0
            if(counter>max):
                max=counter    

        print(counter)
        return max