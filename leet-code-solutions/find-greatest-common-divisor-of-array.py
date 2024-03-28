class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1 = min(nums)    ;   num2 = max(nums)
        def func(num2,num1):
            if num1 == 0:
                return num2
            return func(num1,num2%num1)


        return func(num2,num1)