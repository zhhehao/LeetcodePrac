/*
 * @lc app=leetcode.cn id=453 lang=java
 *
 * [453] 最小移动次数使数组元素相等
 */

// @lc code=start
class Solution {
    public int minMoves(int[] nums) {
        // 数学法
        int moves = 0, min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
        }
        for (int i = 0; i < nums.length; i++) {
            moves += nums[i] - min;
        }
        return moves;

        // 排序
        // Arrays.sort(nums);
        // int ans = 0;
        // for (int i = nums.length-1; i > 0; i--) {
        //     ans += nums[i]-nums[0];
        // }

        // return ans;
    }
}
// @lc code=end

