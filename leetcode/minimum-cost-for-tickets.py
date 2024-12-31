class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)
        def dp(idx):
            if idx >= len(days):
                return 0

            if idx not in memo:
                one = dp(bisect_left(days, days[idx] + 1)) + costs[0]
                seven = dp(bisect_left(days, days[idx] + 7)) + costs[1]
                month = dp(bisect_left(days, days[idx] + 30)) + costs[2]
                memo[idx] = min(one, seven , month)
            return memo[idx]

        return dp(0)


            




