/*
 * @lc app=leetcode.cn id=443 lang=java
 *
 * [443] 压缩字符串
 */

// @lc code=start
class Solution {
    public int compress(char[] chars) {
        if (chars.length == 1) return 1;
        int i = 0, j = 0;
        while (i < chars.length && j < chars.length) {
            char c = chars[j];
            int cnt = 1;
            j++;
            while (j < chars.length && chars[j] == c) {
                cnt++;
                j++;
            }

            chars[i++] = c;
            if (cnt != 1) {           
                String s = "" + cnt;
                for (char cc: s.toCharArray()) {
                    chars[i++] = cc;
                }
            }
        }

        return i;
    }
}
// @lc code=end

