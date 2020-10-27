/*
 * @lc app=leetcode.cn id=45 lang=java
 *
 * [45] 跳跃游戏 II
 */

// @lc code=start
class Solution {
    public int jump(int[] nums) {
        // 正向查找
        int length = nums.length;
        int end = 0;
        int maxPosition = 0;
        int steps = 0;
        for (int i = 0; i < length - 1; i++) {
            maxPosition = Math.max(maxPosition, i + nums[i]);
            if (i == end) {
                end = maxPosition;
                steps++;
            }
        }
        return steps;

        // // 反向查找
        // if (nums.length == 1) return 0;
        // int firstStep = nums[0], right = nums.length - 1;
        // int ans = 0;
        // while (firstStep < right) {
        //     for (int i = 1; i < right; i++) {
        //         if (nums[i] >= right - i) {
        //             ans++;
        //             right = i;
        //             break;
        //         }
        //     }
        // }
        // return ++ans;
    }
}
// @lc code=end

