#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [['Q']]
        
        queens = []
        ans = []

        cols = [False] * n
        dia_minus = {k:False for k in range(1-n, n)}
        dia_plus = {k:False for k in range(0, 2*n-1)}

        def solve(N):
            if N == n:
                rec = []
                for i in range(n):
                    line = ''
                    for j in range(n):
                        if (i,j) in queens:
                            line += 'Q'
                        else:
                            line += '.'
                    rec.append(line)
                ans.append(rec)

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
        return ans

                    
# @lc code=end

