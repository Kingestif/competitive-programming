class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half):
            # basically implement 2 pointers sort these 2 lists 
            l = 0    ;   r = 0   ; ans = []

            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    ans.append(left_half[l])
                    l += 1
                else:
                    ans.append(right_half[r])
                    r += 1
            ans.extend(left_half[l:])
            ans.extend(right_half[r:])

            return ans
        
        def func(left,right,nums):
            if left == right:   #same index so we just have single e/t so return that
                return [nums[left]]
            
            mid = left + (right - left) // 2 #refer on binary search, we said left to avoid overflow
            left_half = func(left,mid,nums)     #make your left_half
            right_half = func(mid + 1, right,nums)

            return merge(left_half,right_half) #pass this to merget function to implement 2 pointers to sort the splitted list
            



        return func(0,len(nums) -1 , nums)

