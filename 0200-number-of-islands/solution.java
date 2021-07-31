class Solution {
    /**
     * @time  : O(nm)
     * @space : O(nm)
     */
    
    char[][] map;

    public int numIslands(char[][] grid) {
        int count = 0;
        
        map = grid;
        
        for(int i=0 ; i<grid.length ; i++) {
            for(int j=0 ; j<grid[0].length ; j++) {
                if(grid[i][j] == '1') {
                    count++;
                    explore(i, j);
                }
            }
        }
        
        return count;
    }
    
    public void explore(int x, int y) {
        if(x<0 || y<0 || x>= map.length || y>= map[0].length) {
            return;
        }
        
        if(map[x][y] == '0') {
            return;
        }
        
        map[x][y] = '0';
        
        explore(x-1, y);
        explore(x+1, y);
        explore(x,   y-1);
        explore(x,   y+1);
        
        return;
    }
}