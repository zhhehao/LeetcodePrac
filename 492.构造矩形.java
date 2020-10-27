/*
 * @lc app=leetcode.cn id=492 lang=java
 *
 * [492] 构造矩形
 */

// @lc code=start
class Solution {
    public int[] constructRectangle(int area) {
        int lo = 1;
        int hi = area;
        while (lo < hi) {
            int i = 1;
            while (area % (lo + i) != 0) i++;
            lo += i;
            hi = area / lo;
            if (lo >= hi) break;
        }
        return new int[]{lo, hi};
    }
}
// @lc code=end

