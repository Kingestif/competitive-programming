class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = []
        dic = defaultdict(int)
        for i in s:
            if i not in dic:
                dic[i] += 1
            else:
                ans.append(i)

        return ans[0]
               