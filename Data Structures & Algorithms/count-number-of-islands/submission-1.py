class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands=0
        visit=set()
        rows,cols=len(grid),len(grid[0])
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if((nr,nc) not in visit and nc in range(cols) and nr in range(rows) and grid[nr][nc]=='1'):
                        visit.add((nr,nc))
                        q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]=='1':
                    bfs(r,c)
                    islands+=1
        return islands