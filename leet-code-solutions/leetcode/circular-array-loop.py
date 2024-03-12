class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            if i not in check:
                check.add(i)
                cycle = set()
                while True:
                    if i in cycle:
                        return True
                    
                    cycle.add(i)
                    #to hold our previous index, and calculate next index
                    prev = i
                    i = (i + nums[i]) % len(nums)
                    if prev == i:   #case 1: means it unicycle and unicycle is not considered cycle
                        break
                    elif nums[prev] > 0 and nums[i] < 0: #case 2: means if cycles have d/t sign its not cycle anymore
                        break
        return False


                        



