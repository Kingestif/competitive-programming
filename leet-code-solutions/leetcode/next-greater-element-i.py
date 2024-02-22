class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Core: used decreasing stack so when element gets thrown by another larger number it means that number is next greater elemetn of the popped item 
        stack=[]
        arr=[-1] * len(nums1)
        map={}
        
        # store the index of the nums1 elements
        for i in range(len(nums1)):
            map[nums1[i]] = i

        def push(x):
            if len(stack) == 0:
                stack.append(x)
            elif x < stack[-1]:
                stack.append(x)
            else:
                while len(stack) > 0 and x > stack[-1]:
                    num = stack[-1]
                    stack.pop()
                    if num in map:
                        arr[map[num]] = x
                stack.append(x)

        for i in range(len(nums2)):
            push(nums2[i])
        
        return arr