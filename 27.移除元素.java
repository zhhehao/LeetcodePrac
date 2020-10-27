/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {

        int i = 0; 
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;

        // if (nums == null || nums.length == 0) return 0;

        // int pos = 0;
        // int next = 0;
        // while (true) {
        //     pos = getPosition(nums, val, pos);
        //     if (pos == nums.length) return nums.length;
        //     next = getDiffVal(nums, val, pos+1);
        //     if (next == nums.length) return pos;
        //     nums[pos] = nums[next];
        //     nums[next] = val;
        //     pos++;
        // } 
        
    }

    // private int getPosition(int[] nums, int val, int start) {
    //     for (int i = start; i < nums.length; i++) {
    //         if (nums[i] == val) 
    //             return i;
    //     }
    //     return nums.length;
    // }

    // private int getDiffVal(int[] nums, int val, int start) {
    //     for (int i = start; i < nums.length; i++) {
    //         if (nums[i] != val)
    //             return i;
    //     }
    //     return nums.length;
    // }
}
// @lc code=end

