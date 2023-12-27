class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # bruteforce
        new=[]
        for i in arr2:
            for j in arr1:
                if j == i:
                    new.append(j)

        arr1.sort()
        for i in arr1:
            if i not in arr2:
                new.append(i)

        return new



        