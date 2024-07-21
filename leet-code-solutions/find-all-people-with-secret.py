class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        sc = set([0,firstPerson])
        map = {}

        for src, dst, t in meetings:
            if t not in map:
                map[t] = defaultdict(list)
            map[t][src].append(dst)
            map[t][dst].append(src)

        def dfs(src, adj):
            if src in visit:
                return 
            visit.add(src)
            sc.add(src)
            for neg in adj[src]:
                dfs(neg,adj)

        for t in sorted(map.keys()):
            visit = set()
            for src in map[t]:
                if src in sc:
                    dfs(src, map[t])

        return list(sc)
