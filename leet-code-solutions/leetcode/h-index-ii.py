class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = []
        if sum(citations) == 0:
            return 0

        def API(mid):
            counter = 0
            # for num in citations:
            #     if num >= mid:
            #         counter += 1
            for i in range(len(citations)):
                if citations[i] >= mid:
                    counter = len(citations) - i 
                    break

            if counter >= mid:
                ans.append(mid)
                return False
            else:
                return True

        start = 1; end = len(citations) 
        while start <= end:
            mid = (start + end) //2
            if API(mid):
                end = mid - 1
            else:
                start = mid + 1
        return ans[-1]
