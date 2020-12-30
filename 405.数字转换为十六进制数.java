/*
 * @lc app=leetcode.cn id=405 lang=java
 *
 * [405] 数字转换为十六进制数
 */

// @lc code=start
class Solution {
    public String toHex(int num) {
        if (num == 0) return "0";
        char[] chex = "0123456789abcdef".toCharArray();

        String ans = "";

        while (num != 0) {
            ans = chex[num & 15] + ans;
            num >>>= 4;
        }

        return ans;
    }
}
// @lc code=end

