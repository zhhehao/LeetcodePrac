/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        if (x == 0)
            return true;
        String s = Integer.toString(x);

        for (int lo = 0, hi = s.length()-1; lo <= hi; lo++, hi--) {
            if (s.charAt(lo) != s.charAt(hi)) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

