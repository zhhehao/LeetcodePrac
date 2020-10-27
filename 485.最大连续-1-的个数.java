/*
 * @lc app=leetcode.cn id=485 lang=java
 *
 * [485] 最大连续1的个数
 */

// @lc code=start
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int ans = 0;
        int con = 0;
        for (int i : nums) {
            if (i == 0) {
                ans = Math.max(ans, con);
                con = 0;
            } else {
                con++;
            }
        }
        return Math.max(ans, con);
    }
}
// @lc code=end

