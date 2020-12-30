import java.util.Arrays;
import java.util.List;

/*
 * @lc app=leetcode.cn id=448 lang=java
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int newidx = Math.abs(nums[i])-1;
            if (nums[newidx] > 0)
                nums[newidx] *= -1;
        }

        for (int i = 1; i <= nums.length; i++) {
            if (nums[i-1] > 0) {
                ans.add(i);
            }
        }
        return ans;


        // List<Integer> ans = new LinkedList<>();
        // Arrays.sort(nums);
        // for (int i = 1; i <= nums.length; i++) {
        //     if (Arrays.binarySearch(nums, i) < 0) ans.add(i);
        // }
        // return ans;
    }
}
// @lc code=end

