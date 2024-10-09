class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        map = defaultdict(list)
        
        for start,end,time in times:
            map[start].append((end,time))


        distances = {node: float('inf') for node in range(1,n+1)}
        distances[k] = 0
        heap = [(0,k)]
        processed = set()

        while heap:
            total_time, node = heapq.heappop(heap)

            if node in processed:
                continue
            processed.add(node)

            for child,curr_time in map[node]:
                distance = total_time + curr_time

                if distance < distances[child]:
                    distances[child] = distance

                heapq.heappush(heap,(distances[child], child))


        return max(distances.values()) if max(distances.values()) != float('inf') else -1



            


