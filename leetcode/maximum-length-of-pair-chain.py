class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        memo = defaultdict(int)
        
        def dp(i):
            if i >= len(pairs):
                return 0

            # choice1
            notake = dp(i+1)

            # choice2 look for a chain that can insert to above one
            take = 1
            if i in memo:
                return memo[i]

            for j in range(i+1,len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    take = dp(j) + 1
                    break
            memo[i] = max(take,notake)
                
            return memo[i]
   
        return dp(0)