import math
class Solution:
    def countPrimes(self, n: int) -> int:
        # TLE
        # if n==0 or n==1:
        #     return 0
        # counter=0
        # for j in range(2,n):
        #     check=False
        #     for i in range(2,floor(sqrt(j))+1):
        #         if j%i==0:
        #             check=True
        #             counter+=1
        #             break

        # return n-counter-2

        # using siev of erathostense
        nums = [i for i in range(2,n)] 
        for i in range(math.floor(math.sqrt(len(nums)))):
            if nums[i]:
                add = nums[i]
                j = i + add
                while j < len(nums):
                    nums[j] = False
                    j += add

        count = 0
        for i in nums:
            if i: count += 1
        return count