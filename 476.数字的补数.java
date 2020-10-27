/*
 * @lc app=leetcode.cn id=476 lang=java
 *
 * [476] 数字的补数
 */

// @lc code=start
class Solution {
    public int findComplement(int num) {
        int n = 1;
        int ans = 0;
        while (num > 0) {
            if((num&1) == 0) ans += n;
            num >>>= 1;
            n <<= 1;
        }
        return ans;
    }
}
// @lc code=end

