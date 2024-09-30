class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def func(mid,m):
            prev = 0  ; count = 1
            for i in range(1,len(position)):
                if position[i] - position[prev] >= mid:
                    prev = i
                    count += 1
            return count >= m                    

        # the binary search
        start = 1   ;  end = max(position) - min(position)
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if func(mid,m):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans