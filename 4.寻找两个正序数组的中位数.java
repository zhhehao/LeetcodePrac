/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // 划分数组
        int m = nums1.length, n = nums2.length;
        if (m > n) return findMedianSortedArrays(nums2, nums1);
        int iMin = 0, iMax = m;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = (m + n + 1) / 2 - i;
            if      (j != 0 && i != m && nums2[j-1] > nums1[i]) iMin = i + 1;
            else if (i != 0 && j != n && nums1[i-1] > nums2[j]) iMax = i - 1;
            else {
                int maxLeft = 0;
                if      (i == 0) maxLeft = nums2[j-1];
                else if (j == 0) maxLeft = nums1[i-1];
                else maxLeft = Math.max(nums1[i-1], nums2[j-1]);

                if ((m+n)%2 == 1) return (double)maxLeft;

                int minRight = 0;
                if      (i == m) minRight = nums2[j];
                else if (j == n) minRight = nums1[i];
                else minRight = Math.min(nums1[i], nums2[j]);

                return (maxLeft + minRight) / 2.0;
            }
        }

        return 0.0;


        // // 二分查找
        // int totalLen = nums1.length + nums2.length;
        // if (totalLen % 2 == 1) {
        //     int midIdx = totalLen / 2;
        //     return (double)getKthEle(nums1, nums2, midIdx+1);
        // } else {
        //     int midIdx1 = totalLen / 2 - 1, midIdx2 = totalLen / 2;
        //     return (getKthEle(nums1, nums2, midIdx1+1) + 
        //             getKthEle(nums1, nums2, midIdx2+1)) / 2.0;
        // }
    }

    private int getKthEle(int[] n1, int[] n2, int k) {
        int len1 = n1.length, len2 = n2.length;
        int idx1 = 0, idx2 = 0;

        while (true) {
            if (idx1 == len1) {
                return n2[idx2 + k - 1];
            }
            if (idx2 == len2) {
                return n1[idx1 + k - 1];
            }
            if (k == 1) {
                return Math.min(n1[idx1], n2[idx2]);
            }

            int half = k / 2;
            int newIdx1 = Math.min(idx1 + half, len1) - 1;
            int newIdx2 = Math.min(idx2 + half, len2) - 1;
            int p1 = n1[newIdx1], p2 = n2[newIdx2];
            if (p1 <= p2) {
                k -= (newIdx1 - idx1 + 1);
                idx1 = newIdx1 + 1;
            } else {
                k -= (newIdx2 - idx2 + 1);
                idx2 = newIdx2 + 1;
            }
        }
    }
}
// @lc code=end

