class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        map = Counter(deck)
        minn = min(map.values())
        ans = []
        if minn == 1: return False
        print(map,minn)
        for key,values in map.items():
            if math.gcd(values,minn) == 1:
                return False
            ans.append(math.gcd(values,minn))
        print(ans)
        mn = min(ans)
        for i in ans:
            if i%mn != 0: return False
        return True
