class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        preOR = []
        ans = []
        k = 2 ** maximumBit - 1

        # 1. make prefix sum for the XOR(instead of poping at each iteration)
        preOR = [nums[0]]
        for i in range(1,len(nums)):
            preOR.append(preOR[-1] ^ nums[i])

        # 2. multiply by the formula
        for i in range(len(preOR)-1,-1,-1):
            ans.append(preOR[i] ^ k)


        return ans







