class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
    #     0       1
    #    0  1    1  0
    #    this are the cases, notice whenever we iterate to left the base number doesnt change but if we iter to right 0 change to 1 and viceversa
    # so we can use binary search 

        curr = 0    #like base case
        start = 1 ; end = 2**(n -1)

        for i in range(n):
            mid = (start + end) // 2
            if k > mid:
                start = mid + 1

                if curr == 0: curr = 1  #previous said we only change values when we move to the right side, so now it happens
                else:   curr = 0
            else:
                end = mid   #moving to out pointer to left side so no need to update curr

        return curr


        