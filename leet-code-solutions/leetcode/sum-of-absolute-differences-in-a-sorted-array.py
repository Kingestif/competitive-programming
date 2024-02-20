class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # Core:just come up with a formula for starting, ending numbers , then for middle number we can use add the above 2 fomulas
        prefix=[]
        ans=[]
        total=0
        # calculate prefix sum
        for i in nums:
            total += i
            prefix.append(total)

        # formula for starting, ending and middle numbers
        for i in range(len(nums)):
            if i == 0:
                ans.append(prefix[-1] - nums[0] * len(nums))
            elif i == len(nums) -1:
                ans.append(nums[i] * i - prefix[i-1])
            else:
                answer = (prefix[-1] - prefix[i]) - (nums[i] * (len(nums) - i - 1))
                answer += (nums[i] * i) - prefix[i-1]
                ans.append(answer)
        return ans
