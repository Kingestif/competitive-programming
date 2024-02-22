from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map= defaultdict(int)
        for i in s:
            if i not in map:
                map[i] = s.rfind(i)
        print(map)
        last = map[s[0]]
        ans=[]
        new=[]
        for i in range(len(s)):
            if i <= last:
                new.append(s[i])
                if map[s[i]] > last:
                    last = map[s[i]]
            else:
                ans.append(len(new))
                new=[]
                new.append(s[i])
                last = map[s[i]]

        ans.append(len(new))
        print(ans)
        return ans

