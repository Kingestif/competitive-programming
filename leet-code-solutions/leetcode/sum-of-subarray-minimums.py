from collections import defaultdict
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Refer Fraz(need only 1 formula to do that)
        ls = [] ; mon = [len(arr)]*len(arr)    #to find next smaller, just decreasing mon stack
        mon2 = [-1]*len(arr)     #to find previous smaller

        # to find next smaller e/t
        def push(i):
            if len(ls) == 0:
                ls.append(i)
            elif arr[i] >= arr[ls[-1]]: 
                mon2[i] = ls[-1]
                ls.append(i)
            else:
                while len(ls) and arr[i] < arr[ls[-1]]:
                    mon[ls[-1]] = i
                    ls.pop()

                if len(ls) != 0:
                    mon2[i] = ls[-1]

                ls.append(i)

        for i in range(len(arr)):
            push(i)

        total = 0
        for i in range(len(mon)):
            count = (i - mon[i]) * (mon2[i] - i)
            total += arr[i] * count

        return total % (10 ** 9 + 7)




        