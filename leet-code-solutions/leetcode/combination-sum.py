class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Core: we want a duplicate so on our formula we dont have to increment "i" out loop will auto increment to handle that
        ans = [] ; summ = 0 
        def backtrack(i, combo , summ):
            if summ == target:
                ans.append(combo[:])   # ":" is same as combo.copy()
                return 
            
            elif summ > target:
                return 

            for i in range(i,len(candidates)):
                combo.append(candidates[i])
                summ += candidates[i]
                backtrack(i , combo,summ)
                
                summ -= combo.pop()
                
                

        backtrack(0,[],summ)
        return ans