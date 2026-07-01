from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # Step 1: Multi-source BFS to compute distance from nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2: Max Heap for safest path
        heap = [(-dist[0][0], 0, 0)]   # negative because Python has min heap
        visited = set()
        visited.add((0,0))

        while heap:
            safe, x, y = heapq.heappop(heap)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))

                    new_safe = min(safe, dist[nx][ny])
                    heapq.heappush(heap, (-new_safe, nx, ny))