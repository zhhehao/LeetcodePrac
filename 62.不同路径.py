#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 回溯，超时
        # ans = 0
        # fm, fn = m-1, n-1
        # def go_finish(i, j):
        #     nonlocal ans
        #     if i == fm and j == fn:
        #         ans += 1
            
        #     if i < fm:
        #         go_finish(i+1, j)

        #     if j < fn:
        #         go_finish(i, j+1)

        # go_finish(0, 0)
        # return ans

        # 排列组合
        # import math
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

        # 动态规划 动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1]*n] + [[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# @lc code=end

