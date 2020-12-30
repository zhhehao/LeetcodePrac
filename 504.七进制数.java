/*
 * @lc app=leetcode.cn id=504 lang=java
 *
 * [504] 七进制数
 */

// @lc code=start
class Solution {
    public String convertToBase7(int num) {
        if (num <= 6 && num >= -6) return num+"";
        boolean isNeg = false;
        if (num < 0) {
            isNeg = true;
            num  = -num;
        }

        String ans = "";
        while (num > 0) {
            ans = num % 7 + ans;
            num /= 7;
        }
        if (isNeg) ans = "-" + ans;
        return ans;
    }
}
// @lc code=end

