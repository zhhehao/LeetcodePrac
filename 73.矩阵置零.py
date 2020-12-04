#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n == 1:
            return 
        if m == 1 and n != 1:
            flag = False
            for j in range(n):
                if matrix[0][j] == 0:
                    flag = True
                    break
            if flag:
                for j in range(n):
                    matrix[0][j] = 0
            return
        if n == 1 and m != 1:
            flag = False
            for i in range(m):
                if matrix[i][0] == 0:
                    flag = True
                    break
            if flag:
                for i in range(m):
                    matrix[i][0] = 0
            return

        r0, c0 = False, False
        for j in range(n):
            if matrix[0][j] == 0:
                r0 = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                c0 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if r0:
            for j in range(n):
                matrix[0][j] = 0

        if c0:
            for i in range(m):
                matrix[i][0] = 0

        return
# @lc code=end

