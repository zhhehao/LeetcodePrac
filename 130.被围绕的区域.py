# @before-stub-for-debug-begin
from python3problem130 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_not_filling_squares(i, j, m, n, accessed_list):
            not_filling_squares.add((i, j))
            accessed_list.add((i, j))
            if i-1 >= 0 and board[i-1][j] == 'O' and (i-1, j) not in accessed_list:
                get_not_filling_squares(i-1, j, m, n, accessed_list)
            if i+1 < m and board[i+1][j] == 'O' and (i+1, j) not in accessed_list:
                get_not_filling_squares(i+1, j, m, n, accessed_list)
            if j-1 >= 0 and board[i][j-1] == 'O' and (i, j-1) not in accessed_list:
                get_not_filling_squares(i, j-1, m, n, accessed_list)
            if j+1 < n and board[i][j+1] == 'O' and (i, j+1) not in accessed_list:
                get_not_filling_squares(i, j+1, m, n, accessed_list)



        m, n = len(board), len(board[0])
        not_filling_squares = set()
        for j in range(n):
            if board[0][j] == 'O':
                get_not_filling_squares(0, j, m, n, set())
            if board[m-1][j] == 'O':
                get_not_filling_squares(m-1, j, m, n, set())
        
        for i in range(1, m-1):
            if board[i][0] == 'O':
                get_not_filling_squares(i, 0, m, n, set())
            if board[i][n-1] == 'O':
                get_not_filling_squares(i, n-1, m, n, set())


        for i in range(1,m):
            for j in range(1,n):
                if board[i][j] == 'O' and (i, j) not in not_filling_squares:
                    board[i][j] = 'X'

        # print(not_filling_squares)
        # print(board)
        # return board
        


# @lc code=end

