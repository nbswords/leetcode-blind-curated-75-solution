import collections
class Solution:
    def numIslands(self, grid) -> int:
        # BFS, Time O(m*n)
        if not any(grid): return 0
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    queue = collections.deque([(i, j)])
                    grid[i][j] = 0 # mark as visited
                    while queue:
                        x, y = queue.popleft()
                        for r, c in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                                grid[r][c] = 0  # mark as visited
                                queue.append((r, c))
        return count
        # DFS, Time O(m*n)
        # if not any(grid): return 0
        # m, n, count = len(grid), len(grid[0]), 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             count += 1
        #             stack = [(i, j)]
        #             grid[i][j] = '0'  # mark as visited

        #             while stack:
        #                 x, y = stack.pop()
        #                 for r, c in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        #                     if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
        #                         grid[r][c] = '0'  # mark as visited
        #                         stack.append((r, c))

        # return count