/*
 * @lc app=leetcode.cn id=10 lang=java
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
class Solution {
    public boolean isMatch(String s, String p) {
        // 回溯
        // if (p.isEmpty()) return s.isEmpty();
        // boolean first_match = (!s.isEmpty() && 
        //                        (p.charAt(0) == s.charAt(0) ||
        //                        p.charAt(0) == '.'));

        // if (p.length() >= 2 && p.charAt(1) == '*') {
        //     return (isMatch(s, p.substring(2)) ||
        //             (first_match && isMatch(s.substring(1), p)));
        // } else {
        //     return first_match && isMatch(s.substring(1), p.substring(1));
        // }

        // DP 自底向上
        // if (p.isEmpty()) return s.isEmpty();
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;

        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '*' && dp[0][i-1]) {
                dp[0][i+1] = true;
            }
        }

        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i)) {
                    dp[i+1][j+1] = dp[i][j];
                }
                if (p.charAt(j) == '*') {
                    if (p.charAt(j-1) != s.charAt(i) && p.charAt(j-1) != '.') {
                        dp[i+1][j+1] = dp[i+1][j-1];
                    } else {
                        dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
                    }
                }
            }
        }
        
        return dp[s.length()][p.length()];
        


        // if (s.length() == 0 && p.length() == 0) return true;
        // if (s.length() == 0 && p.length() != 0) return false;
        // if (s.length() != 0 && p.length() == 0) return false;
        // int i = 0, j = 0;
        // while (i < s.length() && j < p.length()) {
        //     String pa = "";
        //     if (j < p.length()-1 && p.charAt(j) == '.' && p.charAt(j+1) == '*') {
        //         pa += ".*";
        //         j += 2;
        //     } else if (j < p.length()-1 && p.charAt(j+1) == '*') {
        //         pa = pa + p.charAt(j) + p.charAt(j+1);
        //         j += 2;
        //     } else {
        //         pa += p.charAt(j);
        //         j++;
        //     }
        //     i = matchStr(s, i, pa);
        //     if (i == -1) return false;
        // }

        // if (i == s.length() && j == p.length()) return true;
        // else return false;
    }

    // private int matchStr(String s, int i, String pattern) {
    //     char p = pattern.charAt(0);
    //     if (pattern.length() == 2) {
    //         if (p == '.') {
    //             return s.length();
    //         } else {
    //             if (s.charAt(i) != p) return i;
    //             else {
    //                 while (i < s.length() && s.charAt(i) == p) i++;
    //                 return i;
    //             }
    //         }
    //     } else if (p == '.') {
    //         return i+1;
    //     } else {
    //         if (s.charAt(i) != p ) return -1;
    //         else return i+1;
    //     }
    // }
}
// @lc code=end

