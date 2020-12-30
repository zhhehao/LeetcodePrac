/*
 * @lc app=leetcode.cn id=35 lang=java
 *
 * [35] 搜索插入位置
 */

// @lc code=start
class Solution {
    public int searchInsert(int[] nums, int target) {
        if (target <= nums[0]) return 0;
        if (target == nums[nums.length-1]) return nums.length-1;
        if (target > nums[nums.length-1]) return nums.length;

        return spliteSearch(nums, 0, nums.length-1, target);

    }

    private int spliteSearch(int[] nums, int lo, int hi, int target) {
        if (lo >= hi)  {
            return lo;
        }
            
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] > target) {
            hi = mid;
            return spliteSearch(nums, lo, hi, target);
        } else if (nums[mid] < target) {
            lo = mid + 1;
            return spliteSearch(nums, lo, hi, target);
        }

        return -1;
    }
}
// @lc code=end

