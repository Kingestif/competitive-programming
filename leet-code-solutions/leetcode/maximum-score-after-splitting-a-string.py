class Solution:
    def maxScore(self, s: str) -> int:
        nums=list(map(int,list(s)))
        print(nums)
        n=len(nums)
        max=float('-inf')
        imax=[]

        left=nums[:0] ; right = nums[0:n]
        left_count=left.count(0)
        right_count=right.count(1)

        add = left_count + right_count

        if add >= max:
            imax.append(0)
            max=0

        for i in range(len(nums)-1):
            if nums[i] == 0:  #means we append 0 to left
                left_count+=1
            else:       #means we remove 1 from right
                right_count-=1

            add = left_count + right_count

            if add == max:
                imax.append(i+1)
            elif add > max:
                imax.clear()
                imax.append(i+1)
                max=add

        return max