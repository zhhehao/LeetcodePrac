import java.util.Arrays;
import java.util.Collections;

/*
 * @lc app=leetcode.cn id=506 lang=java
 *
 * [506] 相对名次
 */

// @lc code=start
class Solution {
    public String[] findRelativeRanks(int[] nums) {
        Integer[] sort_nums = new Integer[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            sort_nums[i] = nums[i];
        }

        Arrays.sort(sort_nums);

        String[] ans = new String[nums.length];

        for (int i = 0; i < nums.length; i++) {
            int idx = Arrays.binarySearch(sort_nums, nums[i]);
            if (idx == nums.length-1){
                ans[i] = "Gold Medal";
            } else if (idx == nums.length-2) {
                ans[i] = "Silver Medal";
            } else if (idx == nums.length-3) {
                ans[i] = "Bronze Medal";
            } else {
                ans[i] = "" + (nums.length-idx);
            }
        }

        return ans;

        

    }
}
// @lc code=end

