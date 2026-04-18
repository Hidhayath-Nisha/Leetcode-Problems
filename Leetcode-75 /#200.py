class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        island = 0
        directions = [[0,1], [0,-1], [-1,0], [1,0]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    q.append((i,j))
                    grid[i][j] = "0"
                    island += 1
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc

                            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
                                q.append((nr,nc))
                                grid[nr][nc] = "0"
                            
        return island
