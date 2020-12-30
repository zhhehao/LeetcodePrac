/*
 * @lc app=leetcode.cn id=37 lang=java
 *
 * [37] 解数独
 */

// @lc code=start
class Solution {
    public void solveSudoku(char[][] board) {
        int[][] rows = new int[9][9];
        int[][] cols = new int[9][9];
        int[][] sbox = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                int num = board[i][j] - '1';
                int idx_box = (i/3)*3 + j/3;
                rows[i][num] = 1;
                cols[j][num] = 1;
                sbox[idx_box][num] = 1;
            }
        }

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    if (fillSudoku(board, rows, cols, sbox, i, j)) return;
                    
                }
            }
        }
    }

    private boolean fillSudoku(char[][] board, int[][] rows, int[][] cols, int[][] sbox, int i, int j) {
        for (int k = 0; k < 9; k++) {
            if (rows[i][k] == 1) continue;
            if (cols[j][k] == 1) continue;
            int idx_box = (i/3) * 3 + j / 3;
            if (sbox[idx_box][k] == 1) continue;

            board[i][j] = (char)('1' + k);
            rows[i][k] = 1;
            cols[j][k] = 1;
            sbox[idx_box][k] = 1;

            int nextI = -1, nextJ = -1;
            for (int newI = 0; newI < 9; newI++) {
                boolean find = false;
                for (int newJ = 0; newJ < 9; newJ++) {
                    if (board[newI][newJ] == '.') {
                        nextI = newI;
                        nextJ = newJ;
                        find = true;
                        break;
                    }
                }
                if (find) break;
            }
            if (nextI == -1) return true;
            if(fillSudoku(board, rows, cols, sbox, nextI, nextJ)) return true;
            board[i][j] = '.';
            rows[i][k] = 0;
            cols[j][k] = 0;
            sbox[idx_box][k] = 0;
        }

        return false;
    }
}
// @lc code=end

