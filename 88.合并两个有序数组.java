/*
 * @lc app=leetcode.cn id=88 lang=java
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int k = m + n - 1;
        m--;
        n--;

        while (k >= 0) {
            if (m < 0) {
                nums1[k] = nums2[n];
                k--;
                n--;
            } else if (n < 0) {
                nums1[k] = nums1[m];
                k--;
                m--;
            } else {
                if (nums1[m] >= nums2[n]) {
                    nums1[k] = nums1[m];
                    m--;
                } else {
                    nums1[k] = nums2[n];
                    n--;
                }
                k--;
            }
        }
    }
}
// @lc code=end

