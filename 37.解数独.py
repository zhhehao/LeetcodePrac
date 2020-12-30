#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        list_row = [{str(num):False for num in range(1, 10)} for _ in range(9)]
        list_col = [{str(num):False for num in range(1, 10)} for _ in range(9)]
        list_square = [{str(num): False for num in range(1, 10)} for _ in range(9)]
        blank_space = list()

        for i in range (9):
            for j in range(9):
                if board[i][j] in '123456789':
                    k = (i // 3) * 3 + j // 3
                    list_row[i][board[i][j]] = True
                    list_col[j][board[i][j]] = True
                    list_square[k][board[i][j]] = True
                else:
                    blank_space.append((i,j))

        def solve():
            if not blank_space:
                return True
            
            i, j = blank_space.pop()
            k = (i // 3) * 3 + j // 3
            for n in '123456789':
                if list_row[i][n] or list_col[j][n] or list_square[k][n]:
                    continue
                list_row[i][n] = True
                list_col[j][n] = True
                list_square[k][n] = True
                board[i][j] = n
                if solve():
                    return True
                list_row[i][n] = False
                list_col[j][n] = False
                list_square[k][n] = False
                board[i][j] = '.'
            blank_space.append((i, j))
            return False   

        solve()
        


# @lc code=end

