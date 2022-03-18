class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # (base case)
        if len(grid) == 1 and len(grid[0]) == 1: return 1 if grid[0][0] == "1" else 0

        # ==================================================
        #  BFS                                             =
        # ==================================================
        # time  : O(mn)
        # space : O(mn)

        x = len(grid[0])
        y = len(grid)

        ans = 0

        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    ans += 1

                    visited = set()
                    visited.add( (i, j) )

                    while visited:
                        row, col = visited.pop()
                        grid[row][col] = '0'

                        if row   > 0 and grid[row-1][col] == '1': visited.add( (row-1, col) )
                        if row+1 < y and grid[row+1][col] == '1': visited.add( (row+1, col) )
                        if col   > 0 and grid[row][col-1] == '1': visited.add( (row, col-1) )
                        if col+1 < x and grid[row][col+1] == '1': visited.add( (row, col+1) )

        return ans

    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        # (base case)
        if len(grid) == 1 and len(grid[0]) == 1: return 1 if grid[0][0] == "1" else 0

        # ==================================================
        #  DFS                                             =
        # ==================================================
        # time  : O(mn)
        # space : O(mn)

        island = 0
        self.grid = grid

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.explore(i, j)
                    island += 1

        return island

    def explore(self, y: int, x: int) -> None:
        self.grid[y][x] = 0

        if y > 0                     and self.grid[y-1][x] == '1': self.explore(y-1, x)
        if y < len(self.grid) - 1    and self.grid[y+1][x] == '1': self.explore(y+1, x)
        if x > 0                     and self.grid[y][x-1] == '1': self.explore(y, x-1)
        if x < len(self.grid[0]) - 1 and self.grid[y][x+1] == '1': self.explore(y, x+1)
    '''
