#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[False] * n for _ in range(n)]
        num = 1
        end = n ** 2
        i, j = 0, -1
        fx = 'e'
        while num <= end:
            ni, nj = i, j
            if fx == 'e':
                ni, nj = i, j+1
                if nj == n or ans[ni][nj] != False:
                    ni, nj = i+1, j
                    fx = 's'
            elif fx == 's':
                ni, nj = i+1, j
                if ni == n or ans[ni][nj] != False:
                    ni, nj = i, j-1
                    fx = 'w'
            elif fx == 'w':
                ni, nj = i, j-1
                if nj < 0 or ans[ni][nj] != False:
                    ni, nj = i-1, j
                    fx = 'n'
            else:
                ni, nj = i-1, j
                if ni < 0 or ans[ni][nj] != False:
                    ni, nj = i, j+1
                    fx = 'e'
            # print('(%d, %d)' % (ni, nj))
            ans[ni][nj] = num
            num += 1
            i, j = ni, nj

        return ans

# @lc code=end

