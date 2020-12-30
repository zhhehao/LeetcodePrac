/*
 * @lc app=leetcode.cn id=41 lang=java
 *
 * [41] 缺失的第一个正数
 */

// @lc code=start
class Solution {
    public int firstMissingPositive(int[] nums) {
        // 置换
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i]-1] != nums[i]) {
                int temp = nums[nums[i]-1];
                nums[nums[i]-1] = nums[i];
                nums[i] = temp;
            }
        }

        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return i + 1;
        }

        return n + 1;


        // 原地哈希
        // for (int i = 0; i < nums.length; i++) {
        //     if (nums[i] <= 0) nums[i] = nums.length + 1;
        // }
        // for (int i = 0; i < nums.length; i++) {
        //     int num = Math.abs(nums[i]);
        //     if (num <= nums.length) nums[num-1] = -Math.abs(nums[num-1]);
        // }
        // for (int i = 0; i < nums.length; i++) {
        //     if (nums[i] > 0) return i + 1;
        // }
        // return nums.length + 1;
    }
}
// @lc code=end

