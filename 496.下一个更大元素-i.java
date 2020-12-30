import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=496 lang=java
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            int idx = findIt(nums2, nums1[i]);
            boolean flag = false;
            for (int j = idx+1; j < nums2.length; j++) {
                if (nums2[j] > nums2[idx]) {
                    ans[i] = nums2[j];
                    flag = true;
                    break;
                }
            }
            if (!flag) ans[i] = -1;
        }

        return ans;
    }

    private int findIt(int[] n, int k) {
        for (int i = 0; i < n.length; i++) {
            if (n[i] == k)  return i;
        }
        return -1;
    }
}
// @lc code=end

