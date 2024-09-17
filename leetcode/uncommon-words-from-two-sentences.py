class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x = Counter(s1.split())
        y = Counter(s2.split())
        ans = []
        for i in s1.split():
            if i not in y and x[i] == 1:
                ans.append(i)
        
        for j in s2.split():
            if j not in x and y[j] == 1:
                ans.append(j)

        return ans