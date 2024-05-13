class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # its basically bruteforce but b/c of memoization we remember the states

        memo = defaultdict(int)
        def dp(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i,j) not in memo:
                if text1[i] == text2[j]:    #if are the same do for the next indeces and check if they are the same
                        memo[(i,j)] = 1 + dp(i+1,j+1)
                else:
                    memo[(i,j)] = max(dp(i+1,j), dp(i,j+1))    #if not the same stand at index i then look for other letters by increment j, OR stand at j and look for similar letters by incrementing i

            return memo[(i,j)]

        return dp(0,0)
                
