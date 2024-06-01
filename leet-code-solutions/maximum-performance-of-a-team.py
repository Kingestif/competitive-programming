class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # core: at each efficiency level (after sorting decreasing) we wanna check if previous added values * current efficiency is the maximum until length of K is reached!!
        # if length surpasses we must pop previous smaller speed b/c obviously to increase our max so we use heap 
        # we will add our efficincy and speed until K is reached then pop after that
        val = []
        for i in range(len(speed)):     #help us sorte based on efficiency
            val.append((efficiency[i],speed[i]))

        val.sort(reverse = True)
        ans ,speed = 0,0
        heap = []

        for eff,sped in val:        
            if len(heap) == k:
                speed -= heappop(heap)
            heappush(heap,sped)
            speed += sped
            ans = max(ans,eff * speed)


        return ans % (10**9 + 7)



            

            