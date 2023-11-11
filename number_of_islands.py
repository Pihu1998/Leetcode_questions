'''
Leetcode problem:
Time complexity: O(n^2)
Solution: BFS with visited
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r,c):
            q= collections.deque()
            visited.add((r,c))
            q.append((r,c))       
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    
                    if ((row+dr) in range(rows) and (col+dc) in range(cols) and (row+dr, col+dc) not in visited and grid[row+dr][col+dc] == "1"):
                        visited.add((row+dr, col+dc))
                        q.append((row+dr, col+dc))
               
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count+=1
                    bfs(i, j) 

        return count        
