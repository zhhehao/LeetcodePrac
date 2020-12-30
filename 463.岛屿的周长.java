/*
 * @lc app=leetcode.cn id=463 lang=java
 *
 * [463] 岛屿的周长
 */

// @lc code=start
class Solution {
    public int islandPerimeter(int[][] grid) {

        
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 0) continue;
                ans += getEdge(grid, i, j);
            }
        }

        return ans;
    }

    private int getEdge(int[][] grid, int i, int j) {
        int ans = 0;
        if (j-1 < 0) ans++;
        else if (j-1 >= 0 && grid[i][j-1] == 0) ans++;
        if (i-1 < 0) ans++;
        else if (i-1 >= 0 && grid[i-1][j] == 0) ans++;
        if (j+1 >= grid[i].length) ans++;
        else if (j+1 < grid[i].length && grid[i][j+1] == 0) ans++;
        if (i+1 >= grid.length) ans++;
        else if (i+1 < grid.length && grid[i+1][j] == 0) ans++;
        return ans;
    }
}
// @lc code=end

