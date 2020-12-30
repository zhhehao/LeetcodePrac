import java.util.Set;

/*
 * @lc app=leetcode.cn id=36 lang=java
 *
 * [36] 有效的数独
 */

// @lc code=start
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] rows = new int[9][9];
        int[][] cols = new int[9][9];
        int[][] sbox = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') continue;
                int n = board[i][j] - '1';
                int idx_box = (i/3)*3 + j/3;
                if (rows[i][n] == 1) return false;
                else rows[i][n] = 1;
                if (cols[j][n] == 1) return false;
                else cols[j][n] = 1;
                if (sbox[idx_box][n] == 1) return false;
                else sbox[idx_box][n] = 1;
            }
        }
        return true;

        // // 检查行
        //     for (int i = 0; i < 9; i++) {
        //         Set<Character> set = new HashSet<>();
        //         for (int j = 0; j < 9; j++) {
        //             if (board[i][j] == '.') continue;
        //             if (set.contains(board[i][j])) return false;
        //             else set.add(board[i][j]);
        //         }
        //     }
        // // 检查列
        //     for (int i = 0; i < 9; i++) {
        //         Set<Character> set = new HashSet<>();
        //         for (int j = 0; j < 9; j++) {
        //             if (board[j][i] == '.') continue;
        //             if (set.contains(board[j][i])) return false;
        //             else set.add(board[j][i]);
        //         }
        //     }
        // // 检查 3X3
        //     for (int i = 0; i < 9; i += 3) {
        //         for (int j = 0; j < 9; j += 3) {
        //             Set<Character> set = new HashSet<>();
        //             for (int p = 0; p < 3; p++) {
        //                 for (int q = 0; q < 3; q++) {
        //                     if (board[i+p][j+q] == '.') continue;
        //                     if (set.contains(board[i+p][j+q])) return false;
        //                     else set.add(board[i+p][j+q]);
        //                 }
        //             }
        //         }
        //     }


        // return true;
    }
}
// @lc code=end

