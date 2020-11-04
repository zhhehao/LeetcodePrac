#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_row = [{str(key): False for key in range(1, 10)} for _ in range(9)]
        list_col = [{str(key): False for key in range(1, 10)} for _ in range(9)]
        list_square = [{str(key): False for key in range(1, 10)} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number == '.':
                    continue
                if list_row[i][number]:
                    return False
                else:
                   list_row[i][number] = True
                if list_col[j][number]:
                    return False
                else:
                    list_col[j][number] = True

                # if 0 <= i <= 2:
                #     if 0 <= j <= 2:
                #         k = 0
                #     elif 3 <= j <= 5:
                #         k = 1
                #     else:
                #         k = 2
                # elif  3 <= i <= 5:
                #     if 0 <= j <= 2:
                #         k = 3
                #     elif 3 <= j <= 5:
                #         k = 4
                #     else:
                #         k = 5
                # else:
                #     if 0 <= j <= 2:
                #         k = 6
                #     elif 3 <= j <= 5:
                #         k = 7
                #     else:
                #         k = 8
                
                k = (i // 3) * 3 + j // 3

                if list_square[k][number]:
                    return False
                else:
                    list_square[k][number] = True

        return True


        
# @lc code=end

