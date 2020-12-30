/*
 * @lc app=leetcode.cn id=31 lang=java
 *
 * [31] 下一个排列
 */

// @lc code=start
class Solution {
    public void nextPermutation(int[] nums) {
        if (nums.length <= 1) return;
        int j = nums.length - 1, i = nums.length - 2, k = nums.length - 1;
        while (i >= 0) {
            if (nums[i] < nums[j]) break;
            i--;
            j--;
        }

        if (i >= 0) {
            while (nums[k] <= nums[i]) k--;
            int temp = nums[k];
            nums[k] = nums[i];
            nums[i] = temp;
        }

        for (int m = j, n = nums.length-1; m < n; m++, n--) {
            int temp = nums[n];
            nums[n] = nums[m];
            nums[m] = temp;
        }

    }
}
// @lc code=end

