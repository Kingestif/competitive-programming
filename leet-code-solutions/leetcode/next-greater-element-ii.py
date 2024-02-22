class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Core: emplement the next greater e/t I, then again for the e/ts left up on your stack(not get popped) do the same again
        stack=[]
        arr=[-1] * len(nums)

        def push(x):
            if len(stack) == 0:
                stack.append(x)
            elif nums[x] < nums[stack[-1]]:
                stack.append(x)
            else:
                while len(stack) > 0 and nums[x] > nums[stack[-1]]:
                    # risk: >=
                    num = stack[-1]
                    arr[num] = nums[x]
                    stack.pop()
                stack.append(x)

        for i in range(len(nums)):
            push(i)
        print(stack)
        
        if len(stack) == 0:
            return arr

        def push2(x):
            if nums[x] > nums[stack[-1]]:
                while len(stack) > 0 and nums[x] > nums[stack[-1]]:
                    num = stack[-1]
                    arr[num] = nums[x]
                    stack.pop()


        for i in range(len(nums)):
            push2(i)
            
        return arr