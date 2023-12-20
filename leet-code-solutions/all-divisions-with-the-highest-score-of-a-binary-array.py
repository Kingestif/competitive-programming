class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # approach1: slicing each iteration(easy but costy)
        # approach1: count only once then update by checking first e/t 
        n=len(nums)
        max=float('-inf')
        imax=[]

        left=nums[:0] ; right = nums[0:n]
        left_count=left.count(0)
        right_count=right.count(1)

        add = left_count + right_count
        print(add)

        if add >= max:
            imax.append(0)
            max=add






        for i in range(len(nums)):

            # left=nums[:i] ; right = nums[i:n]
            # add=left.count(0) + right.count(1)

            # if add == max:
            #     imax.append(i)
            # elif add > max:
            #     imax.clear()
            #     imax.append(i)
            #     max=add

            # print(i,add)
            if nums[i] == 0:  #means we append 0 to left
                left_count+=1
            else:       #means we remove 1 from right
                right_count-=1

            add = left_count + right_count
            print(add)

            if add == max:
                imax.append(i+1)
            elif add > max:
                imax.clear()
                imax.append(i+1)
                max=add

            
        return imax
            
