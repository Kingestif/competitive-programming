class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  ; curMin = nums[0]
        def push(x):
            nonlocal curMin
            
            while stack and x >= stack[-1][0]:
                stack.pop()
            if stack and x > stack[-1][1]:
                return True

            stack.append([x,curMin])
            curMin = min(curMin,x)

                

        for n in nums[1:]:  #started from 1 since the first e/t will not be answer
            if push(n): 
                return True
        return False

        # # to find next greater e/t
        # def push(i):
        #     if len(ls) == 0:
        #         ls.append(i)
        #     elif nums[i] <= nums[ls[-1]]: 
        #         ls.append(i)
        #     else:
        #         while len(ls) and nums[i] > nums[ls[-1]]:
        #             mon[ls[-1]] = i
        #             ls.pop()

        #         ls.append(i)

        # for i in range(len(nums)):
        #     push(i)

        # print(mon)
        # mon2 = [-1]*len(nums)     #to find previous smaller
        # ls2 = []

        # minim = 0
        # def push2(i):
        #     nonlocal minim
        #     if len(ls2) == 0:
        #         ls2.append(i)
        #     elif nums[i] >= nums[ls2[-1]]: 
        #         if nums[ls2[-1]] < nums[minim]:
        #             minim = ls2[-1]
        #         mon2[i] = minim
        #         ls2.append(i)
        #     else:
        #         while len(ls2) and nums[i] < nums[ls2[-1]]:
        #             ls2.pop()

        #         if len(ls2) != 0:
        #             if nums[ls2[-1]] < nums[minim]:
        #                 minim = ls2[-1]

        #             mon2[i] = minim

        #         ls2.append(i)

        # for i in range(len(nums)):
        #     push2(i)
        # print(mon2)

        # for i in range(len(mon)):
        #     start = mon2[i]     ; end = i      ; mid = mon[start]

        #     if start != -1 and mid != len(nums):
        #         if mid > start and mid < end:
        #             return True
        # return False
        