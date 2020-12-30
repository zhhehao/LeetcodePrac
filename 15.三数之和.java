import java.util.List;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // 排序 + 双指针
        int len = nums.length;
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < len; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int k = len - 1;
            int target = -nums[i];

            for (int j = i + 1; j < len; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;

                while (j < k && nums[j] + nums[k] > target) k--;

                if (j == k) break;

                if (nums[j] + nums[k] == target) {
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[j]);
                    list.add(nums[k]);
                    ans.add(list);
                }
            }
        }

        return ans;
    }
}
// @lc code=end

