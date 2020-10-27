/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int ans = 0;
        int i = 0, j = height.length - 1;
        while (i < j) {
            ans = Math.max(ans, (j-i) * Math.min(height[i], height[j]));
            if (height[i] <= height[j]) i++;
            else j--;
        }
        return ans;
    }
}
// @lc code=end

