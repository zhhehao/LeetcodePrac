/*
 * @lc app=leetcode.cn id=415 lang=java
 *
 * [415] 字符串相加
 */

// @lc code=start
class Solution {
    public String addStrings(String num1, String num2) {
        String ans = "";
        int i = num1.length()-1;
        int j = num2.length()-1;
        int up = 0;
        while (i >= 0 || j >= 0) {
            if (i < 0) {
                if (up == 0)
                    ans = num2.charAt(j--) + ans;
                else {
                    int sum = up + num2.charAt(j--) - '0';
                    up = sum / 10;
                    ans = sum % 10 + ans;
                }
            } else if (j < 0) {
                if (up == 0)
                    ans = num1.charAt(i--) + ans;
                else {
                    int sum = up + num1.charAt(i--) - '0';
                    up = sum / 10;
                    ans = sum % 10 + ans;
                }
            } else {
                int sum = up + num1.charAt(i--) + num2.charAt(j--) - '0' - '0';
                up = sum / 10;
                ans = sum % 10 + ans;
            }
        }

        if (up == 0)
            return ans;
        else 
            return up + ans;
    }
}
// @lc code=end

