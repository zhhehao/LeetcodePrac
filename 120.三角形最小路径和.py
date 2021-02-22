#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    # flag = False
    # rec = 0
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # n = len(triangle)-1
        # def solve(i, j, val):
        #     val = val + triangle[i][j]
        #     if i == n:
        #         if not self.flag:
        #             self.rec = val
        #             self.flag = True
        #         else:
        #             self.rec = min(self.rec, val)
        #         return

        #     solve(i+1, j, val)
        #     solve(i+1, j+1, val)

        # solve(0, 0, 0)

        # return self.rec

        # DP

        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[n-1])
# @lc code=end

