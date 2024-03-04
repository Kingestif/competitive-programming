class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = [i for i in range(1,n + 1)]
        ans = []
        def backtrack(i, combo):
            if len(combo) == k:
                ans.append(combo[:])   # ":" is same as combo.copy()
                return 
            if i >= n:
                return 

            # insert (choose)
            combo.append(num[i])
            backtrack(i + 1, combo)

            # not choose
            combo.pop()
            backtrack(i + 1,combo)
            return combo



        backtrack(0,[])
        return ans