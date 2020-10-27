/*
 * @lc app=leetcode.cn id=38 lang=java
 *
 * [38] 外观数列
 */

// @lc code=start
class Solution {
    public String countAndSay(int n) {
        if (n == 1) return "1";
        String s = "1";

        for (int i = 1; i < n; i++) {
            s = readStr(s);
        }

        return s;
    }

    private String readStr(String str) {
        String rev = "";
        for (int i = 0; i < str.length(); ) {
            char c = str.charAt(i);
            int cnt = 0;
            while (i < str.length() && str.charAt(i) == c) {
                i++;
                cnt++;
            }
            rev = rev + cnt + c;
        }
        return rev;
    }
}
// @lc code=end

