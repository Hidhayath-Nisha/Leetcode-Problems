class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [[0,1],[0,-1],[1,0], [-1, 0]]
        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            r, c, steps = q.popleft()
            for i,j in directions:
                nr, nc =  r+i, c+j
                if 0<=nr<rows and 0<=nc<cols:
                    if (nr == 0 or nr == rows -1 or nc == 0 or nc == cols-1) and  maze[nr][nc] == ".":
                        return steps + 1
                    if maze[nr][nc] == ".":
                        q.append([nr,nc,steps+1])
                        maze[nr][nc] = "+"
        return -1
