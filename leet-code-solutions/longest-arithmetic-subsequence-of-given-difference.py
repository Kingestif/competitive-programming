class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # check if it have occured before!! 
        map = defaultdict(int)

        for i in range(len(arr)):
            map[arr[i]] = 1 + map[arr[i]-difference]


        return max(map.values())