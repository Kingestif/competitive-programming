from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total=0 ; arr=[]    ;arr2=[]
        for i in nums:
            if i % 2 == 0:
                arr.append(0)
            else:
                arr.append(1)

        # now we turned the question to "find subarray sum equals k"
        total=0 ; map=defaultdict(int) ; map[0]=1 ; counter=0
        
        for i in range(len(arr)):
            total += arr[i]
            if total - k in map:
                counter += map[total - k]
            map[total] += 1                
        return counter
            


