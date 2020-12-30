/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        // 中心扩散
        int len = s.length();
        if (len < 2) return s;
        
        int maxLen = 1;
        String res = s.substring(0, 1);
        for (int i = 0; i < len - 1; i++) {
            String oddStr = centerSpread(s, i, i);
            String evenStr = centerSpread(s, i, i+1);
            String maxLenStr = oddStr.length() > evenStr.length() ? oddStr : evenStr;
            if (maxLenStr.length() > maxLen) {
                maxLen = maxLenStr.length();
                res = maxLenStr;
            }
        }

        return res;

        // DP
        // int len = s.length();
        // if (len < 2) return s;

        // int maxLen = 1;
        // int begin = 0;

        // boolean[][] dp = new boolean[len][len];
        // char[] ch = s.toCharArray();

        // for (int i = 0; i < len; i++) {
        //     dp[i][i] = true;
        // }

        // for (int j = 1; j < len; j++) {
        //     for (int i = 0; i < j; i++) {
        //         if (ch[i] != ch[j]) dp[i][j] = false;
        //         else {
        //             if (j - i < 3) dp[i][j] = true;
        //             else dp[i][j] = dp[i+1][j-1];
        //         }

        //         if (dp[i][j] && j - i + 1 > maxLen) {
        //             maxLen = j - i + 1;
        //             begin = i;
        //         }
        //     }
        // }

        // return s.substring(begin, begin+maxLen);


        // Brute Force
        // int len = s.length();
        // while (len > 0) {
        //     for (int i = 0; i + len <= s.length(); i++) {
        //         String subStr = s.substring(i, i+len);
        //         if (isPal(subStr)) return subStr;
        //     }
        //     len--;
        // }
        // return "";
    }

    private boolean isPal(String s) {
        int i = 0, j = s.length()-1;
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) return false;
        }
        return true;
    }

    private String centerSpread(String s, int left, int right) {
        int len = s.length();
        int i = left;
        int j = right;
        while (i >= 0 && j < len) {
            if (s.charAt(i) == s.charAt(j)) {
                i--;
                j++;
            } else {
                break;
            }
        }
        return s.substring(i+1, j);
    }
}
// @lc code=end

