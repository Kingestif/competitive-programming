class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        arr = [0] * k

        map = defaultdict(int)
        check = set()
        for x,y in logs:
            if (x,y) not in check:
                check.add((x,y))
                map[x] += 1
                
        for key,values in map.items():
            arr[values-1] += 1

        return arr

