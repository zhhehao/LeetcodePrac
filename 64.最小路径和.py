#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 回溯超时
        # m, n= len(grid), len(grid[0])
        # ans = 0
        # for j in range(n):
        #     ans += grid[0][j]
        # for i in range(1, m):
        #     ans += grid[i][n-1]

        # def solve(sum, i, j):
        #     nonlocal ans
        #     if i == m-1 and j == n-1:
        #         sum += grid[i][j]
        #         ans = min(ans, sum)
        #         return
        #     if i+1 < m and sum < ans:
        #         solve(sum+grid[i][j], i+1, j)
        #     if j+1 < n and sum < ans:
        #         solve(sum+grid[i][j], i, j+1)
        #     return

        # solve(0, 0, 0)
        # return ans

        # DP
        m, n= len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        # dp[0][0] = grid[0][0]
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j == 0 and i > 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                elif i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]

    
# @lc code=end

