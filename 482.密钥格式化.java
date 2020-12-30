/*
 * @lc app=leetcode.cn id=482 lang=java
 *
 * [482] 密钥格式化
 */

// @lc code=start
class Solution {
    public String licenseKeyFormatting(String S, int K) {
        String ans = "";
        int i = S.length()-1;
        int j = K;

        while (i >= 0) {
            char c = S.charAt(i--);
            if (c == '-') continue;
            if (Character.isLetter(c)) {
                c = Character.toUpperCase(c);
            }
            ans = c + ans;
            j--;
            if (j == 0) {
                ans = "-" + ans;
                j = K;
            }
        }
        if (ans.length() != 0 && ans.charAt(0) == '-') return ans.substring(1);
        else return ans;
    }
}
// @lc code=end

