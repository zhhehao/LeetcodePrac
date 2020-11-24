#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    ans = 0

    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        queens = []

        cols = [False] * n
        dia_minus = {k:False for k in range(1-n, n)}
        dia_plus = {k:False for k in range(0, 2*n-1)}

        def solve(N):
            if N == n:
                self.ans += 1
            i = N
            for j in range(n):
                if cols[j] or dia_minus[i-j] or dia_plus[i+j]:
                    continue
                queens.append((i,j))
                cols[j] = True
                dia_minus[i-j] = True
                dia_plus[i+j] = True
                solve(N+1)
                queens.pop()
                cols[j] = False
                dia_minus[i-j] = False
                dia_plus[i+j] = False

        solve(0)
        return self.ans
# @lc code=end

