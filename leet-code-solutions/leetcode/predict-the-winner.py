class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)
        def func(left, right, turn):
            # basecase
            if left > right:
                return 0
            elif (left,right,turn) in visited:
                return visited[(left,right,turn)]

            # recursion
            ans = 0
            # if turn is 1 its player ones turn and we need to maximize our score
            if turn == 1:
                ans = max(nums[left] + func(left + 1, right, 2), nums[right] + func(left, right - 1, 2))

            else:   #its players 2 turn and it want to minimize score of player 1 
                ans = min(func(left + 1, right, 1), func(left, right - 1, 1))

            visited[(left,right,turn)] = ans
            return ans



            



        player1_val = func(0,len(nums) -1, 1)
        return player1_val >= sum(nums) - player1_val



        
        