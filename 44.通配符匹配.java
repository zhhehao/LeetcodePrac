/*
 * @lc app=leetcode.cn id=44 lang=java
 *
 * [44] 通配符匹配
 */

// @lc code=start
class Solution {
    public boolean isMatch(String s, String p) {
        // 贪心
        int sRight = s.length(), pRight = p.length();
        while (sRight > 0 && pRight > 0 && p.charAt(pRight-1) != '*') {
            if (charMatch(s.charAt(sRight-1), p.charAt(pRight-1))) {
                --sRight;
                --pRight;
            } else {
                return false;
            }
        }

        if (pRight == 0) {
            return sRight == 0;
        }

        int sIndex = 0, pIndex = 0;
        int sRecord = -1, pRecord = -1;

        while (sIndex < sRight && pIndex < pRight) {
            if (p.charAt(pIndex) == '*') {
                ++pIndex;
                sRecord = sIndex;
                pRecord = pIndex;
            } else if (charMatch(s.charAt(sIndex), p.charAt(pIndex))) {
                ++sIndex;
                ++pIndex;
            } else if (sRecord != -1 && sRecord + 1 < sRight) {
                ++sRecord;
                sIndex = sRecord;
                pIndex = pRecord;
            } else {
                return false;
            }
        }

        return allStars(p, pIndex, pRight);

        // DP
        // int m = s.length();
        // int n = p.length();
        // boolean[][] dp = new boolean[m+1][n+1];
        // dp[0][0] = true;
        // // 处理 p 全部是 * 的情况
        // for (int i = 1; i <= n; i++) {
        //     if (p.charAt(i-1) == '*') {
        //         dp[0][i] = true;
        //     } else {
        //         break;
        //     }
        // }

        // for (int i = 1; i <= m; ++i) {
        //     for (int j = 1; j <= n; ++j) {
        //         if (p.charAt(j-1) == '*') {
        //             dp[i][j] = dp[i][j-1] || dp[i-1][j];
        //         } else if (p.charAt(j-1) == '?' || s.charAt(i-1) == p.charAt(j-1)) {
        //             dp[i][j] = dp[i-1][j-1];
        //         }
        //     }
        // }

        // return dp[m][n];



        // 超时
        // if (s.isEmpty() && p.isEmpty()) return true;
        // if (p.length() != 0) {
        //     boolean flag = true;
        //     for (int i = 0; i < p.length(); i++) {
        //         if (p.charAt(i) != '*') {flag = false; break;}
        //     }
        //     if (flag) return true;
        // }
        // if (s.isEmpty() || p.isEmpty()) return false;
        // if (p.charAt(0) == '*') { // 此处会超时
        //     for (int i = 0; i <= s.length(); i++) {
        //         if (isMatch(s.substring(i), p.substring(1))) return true;
        //     }
        // } else if (p.charAt(0) == '?') {
        //     if (isMatch(s.substring(1), p.substring(1))) return true;
        // } else {
        //     if (s.charAt(0) == p.charAt(0)) {
        //         if (isMatch(s.substring(1), p.substring(1))) return true;
        //     }
        // }
        // return false;
    }

    public boolean allStars(String str, int left, int right) {
        for (int i = left; i < right; ++i) {
            if (str.charAt(i) != '*') {
                return false;
            }
        }

        return true;
    }

    public boolean charMatch(char u, char v) {
        return u == v || v == '?';
    }
}
// @lc code=end

