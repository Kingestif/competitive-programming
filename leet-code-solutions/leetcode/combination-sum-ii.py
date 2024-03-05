class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = [] ; summ = 0 
        candidates.sort()
        def backtrack(i,combo , summ):
            if summ == target:
                ans.append(combo[:])   # ":" is same as combo.copy()
                return 
            
            elif summ > target:
                return 

            for j in range(i,len(candidates)):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                combo.append(candidates[j])
                summ += candidates[j]
                backtrack(j + 1,combo,summ)
                summ -= combo.pop()
            return combo
           
                
                

        backtrack(0,[],summ)
        return ans