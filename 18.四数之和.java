/*
 * @lc app=leetcode.cn id=18 lang=java
 *
 * [18] 四数之和
 */

// @lc code=start
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i+1; j < nums.length; j++) {
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int newTarget = target - nums[i] - nums[j];
                int right = nums.length - 1;
                for (int left = j + 1; left < nums.length; left++) {
                    if (left > j + 1 && nums[left] == nums[left-1]) continue;
                    while (left < right && nums[left] + nums[right] > newTarget) right--;
                    if (left == right) break;
                    if (nums[left] + nums[right] == newTarget) {
                        List<Integer> list = new ArrayList<>();
                        list.add(nums[i]);
                        list.add(nums[j]);
                        list.add(nums[left]);
                        list.add(nums[right]);
                        ans.add(list);
                    } 
                }
            }
        }

        return ans;
    }
}
// @lc code=end

