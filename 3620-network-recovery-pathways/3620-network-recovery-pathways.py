from typing import List
import heapq

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        costs = []

        for u, v, c in edges:
            graph[u].append((v, c))
            costs.append(c)

        def can(min_edge):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            pq = [(0, 0)]   # (cost, node)

            while pq:
                curr_cost, node = heapq.heappop(pq)

                if curr_cost > dist[node]:
                    continue

                for nei, cost in graph[node]:
                    # edge cost threshold
                    if cost < min_edge:
                        continue

                    # intermediate nodes online hone chahiye
                    if nei != n - 1 and not online[nei]:
                        continue

                    new_cost = curr_cost + cost

                    if new_cost < dist[nei] and new_cost <= k:
                        dist[nei] = new_cost
                        heapq.heappush(pq, (new_cost, nei))

            return dist[n - 1] <= k

        if not costs:
            return -1

        left, right = 0, max(costs)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans