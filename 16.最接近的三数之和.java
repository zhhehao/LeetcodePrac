/*
 * @lc app=leetcode.cn id=16 lang=java
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int len = nums.length;
        Arrays.sort(nums);
        // if (target <= nums[0]) return nums[0] + nums[1] + nums[2];
        // if (target >= nums[len-1]) return nums[len-1] + nums[len-2] + nums[len-3];

        int ans = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < len; i++) {
            int j = i + 1, k = len - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (Math.abs(sum-target) < Math.abs(ans-target)) ans = sum;
                if (sum == target) return target;
                if (sum > target) k--;
                if (sum < target) j++;
            }

        }
        
        return ans;
    }
}
// @lc code=end

