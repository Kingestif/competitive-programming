from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.ans = []
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value,timestamp])
        # print(self.map)
        
        

    def get(self, key: str, timestamp: int) -> str:
        start = 0 ; end = len(self.map[key])-1
        while start <= end:
            mid = (start + end) // 2
            if timestamp > self.map[key][mid][1] :
                start = mid + 1
                ans = mid
                self.ans.append(self.map[key][mid][0])
            elif timestamp < self.map[key][mid][1]:
                end = mid - 1
            else:
                return self.map[key][mid][0]

        if len(self.ans) == 0:
            return ""
        else:
            return self.ans[-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)