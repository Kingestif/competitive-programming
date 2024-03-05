class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = [] ; summ =0
        def backtrack(i,combo,summ):
            if summ == n and len(combo) == k:
                ans.append(combo[:])
                return
            # elif summ > n:
            #     return 

            for j in range(i,10):
                combo.append(j)
                summ += j
                backtrack(j + 1, combo,summ)
                summ -= combo.pop()

            

        backtrack(1,[],summ)
        return ans