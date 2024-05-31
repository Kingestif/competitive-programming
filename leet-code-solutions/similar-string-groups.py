class UnionFind:
    def __init__(self, size):   #just basic union find code
        self.root = list(range(size))

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(s1, s2):    #if we were give only 2 string this code only handles that
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                if len(diff) > 2:   #since we are asked atmost 2
                    return False
            return len(diff) == 2 or len(diff) == 0

        n = len(strs)
        uf = UnionFind(n)   
        
        for i in range(n):      #use bruteforce to group similar strings 
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    uf.union(i, j)

        # the length basically means the number of groups
        map = defaultdict(int)
        for i in range(n):
            map[uf.find(i)] = 1

        return len((map))

