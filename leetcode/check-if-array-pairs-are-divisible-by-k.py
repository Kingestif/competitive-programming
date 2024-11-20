from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        map = defaultdict(int)
        
        for i in arr:
            remainder = i % k
            if remainder < 0:
                remainder += k
            map[remainder] += 1
        
        total_pairs = 0
        for i in arr:
            remainder = i % k
            if remainder < 0:
                remainder += k
            
            complement = (k - remainder) % k
            if map[remainder] > 0 and map[complement] > 0:
                if remainder == complement:
                    if map[remainder] >= 2:
                        total_pairs += 1
                        map[remainder] -= 2
                else:
                    total_pairs += 1
                    map[remainder] -= 1
                    map[complement] -= 1

        return total_pairs == len(arr) // 2
