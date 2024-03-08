from collections import defaultdict
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.map = defaultdict(list)
        self.dict = defaultdict(int)
        self.time = times
        self.person = persons

        ls = [] ; maxi = float("-inf")
        self.mx = [] ; check = defaultdict(int)  ; dupl = defaultdict(int)   ; self.tf = [] ; maxx = defaultdict(int)
        self.ans = defaultdict(int)
        for i in range(len(self.time)):
            check[self.person[i]] += 1
            maxx[self.person[i]] += 1
            if maxx[self.person[i]] >= maxi:
                maxi = maxx[self.person[i]]
                lastMax = [self.person[i],maxi]
                currWin = self.person[i]
            self.mx.append(currWin)


            if check[self.person[i]] not in dupl:
                self.tf.append(0)
            else:
                self.tf.append(1)
            dupl[check[self.person[i]]] = 1

            ls.append(self.person[i])
            self.map[self.time[i]]= ls.copy()

            self.ans[self.time[i]] = currWin


        print("maxxxx:",self.mx)
        print("ansss", self.ans)

    def q(self, t: int) -> int:
        x = bisect_right(self.time,t) - 1
        y = self.time[x]
        print("timer",y)
        return self.ans[y] 
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)