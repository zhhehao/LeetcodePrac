/*
 * @lc app=leetcode.cn id=414 lang=java
 *
 * [414] 第三大的数
 */

// @lc code=start
class Solution {
    public int thirdMax(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int n1 = Integer.MIN_VALUE;
        int n2 = Integer.MIN_VALUE;
        int n3 = Integer.MIN_VALUE;

        boolean flag = false;

        for (int n : nums) {
            if (n == Integer.MIN_VALUE) flag = true;
            if (n > n1) {
                n3 = n2;
                n2 = n1;
                n1 = n;
            }
            else if (n < n1 && n > n2) {
                n3 = n2;
                n2 = n;
            }
            else if (n < n1 && n < n2 && n > n3) {
                n3 = n;
            }
        }

        if (n3 != Integer.MIN_VALUE) return n3;
        else if (n2 > n3 && flag) return n3; 
        else return n1; 


    }
}
// @lc code=end

