class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(divisors)):
            for j in nums:
                if j%divisors[i] == 0:
                    dic[(divisors[i],i)] += 1
        if len(dic) <1:
            return min(divisors)

        val = max(dic.values())

        ans = []
        for key,values in dic.items():
            if values == val:
                ans.append(key[0])
        return min(ans)
        