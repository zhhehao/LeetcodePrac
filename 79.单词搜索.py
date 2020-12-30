# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        used = [[False] * n for _ in range(m)]
        wl = len(word)
        def solve(x, y, i):
            print(word[i])
            if board[x][y] != word[i]:
                return False
            used[x][y] = True
            if wl == i + 1:
                return True
            if x > 0 and not used[x-1][y]:
                used[x-1][y] = True
                if solve(x-1, y, i+1):
                    return True
                used[x-1][y] = False
            if x < m-1 and not used[x+1][y]:
                used[x+1][y] = True
                if solve(x+1, y, i+1):
                    return True
                used[x+1][y] = False
            if y > 0 and not used[x][y-1]:
                used[x][y-1] = True
                if solve(x, y-1, i+1):
                    return True
                used[x][y-1] = False
            if y < n-1 and not used[x][y+1]:
                used[x][y+1] = True
                if solve(x, y+1, i+1):
                    return True
                used[x][y+1] = False
            used[x][y] = False
            return False

        for j in range(m):
            for k in range(n):
                if solve(j, k, 0):
                    return True

        return False



# @lc code=end

