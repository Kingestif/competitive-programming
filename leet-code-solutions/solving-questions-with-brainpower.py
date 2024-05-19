class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # understanding the question is the hardest part
        # it says return maximize your points, points are arr[i][0], the downside is when you index i's point you must skip next indexes by + arr[i][1] 
        # ex at first if you take index 0 points = 3 and youll skip to 0 + 2, the 3rd index (0'indexed) then points = 3 + 2 and skip will be 3 + 5.....
        memo = defaultdict(int)
        def dp(idx):
            if idx >= len(questions):
                return 0
            
            if idx not in memo:
                memo[idx] = max(dp(idx + 1 +questions[idx][1]) + questions[idx][0], dp(idx+1))
            return memo[idx]

        return dp(0)