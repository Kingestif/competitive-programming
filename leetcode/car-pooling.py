class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        new=[0]*1002

        for row in trips:
            new[row[1]] += row[0]
            new[row[2]] -= row[0]
        total=0
        
        for i in range(len(new)):
            total += new[i]
            new[i] = total

        for i in new:
            if i > capacity:
                return False
        return True





