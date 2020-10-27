/*
 * @lc app=leetcode.cn id=6 lang=java
 *
 * [6] Z 字形变换
 */

// @lc code=start
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        String[] res = new String[numRows];
        for (int j = 0; j < numRows; j++) res[j] = "";
        int i = 0;
        boolean up = false;

        for (int j = 0; j < s.length(); j++) {
            res[i] += s.charAt(j);
            if (i == 0) {
                i++;
                up = false;
            } else if (i == numRows-1) {
                i--;
                up = true;
            } else {
                if (up) i--;
                else i++;
            }
        }

        String ans = "";
        for (int j = 0; j < numRows; j++) {
            ans += res[j];
        }
        return ans;
    }
}
// @lc code=end

