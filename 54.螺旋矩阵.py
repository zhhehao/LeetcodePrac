# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        fangxiang = 'e'
        m = len(matrix)
        n = len(matrix[0])
        size = m * n
        ans = []
        ans.append(matrix[i][j])
        matrix[i][j] = None
        cnt = 1
        while cnt < size:
            if fangxiang == 'e':
                if j == n-1 or matrix[i][j+1] == None:
                    i += 1
                    fangxiang = 's'
                else:
                    j += 1
            elif fangxiang == 's':
                if i == m-1 or matrix[i+1][j] == None:
                    j -= 1
                    fangxiang = 'w'
                else:
                    i += 1
            elif fangxiang == 'w':
                if j == 0 or matrix[i][j-1] == None:
                    i -= 1
                    fangxiang = 'n'
                else:
                    j -= 1
            else:
                if i == 0 or matrix[i-1][j] == None:
                    j += 1
                    fangxiang = 'e'
                else:
                    i -= 1
            # print(i, j)
            ans.append(matrix[i][j])
            matrix[i][j] = None
            cnt += 1

        return ans
                

# @lc code=end

