/*
 * @lc app=leetcode.cn id=507 lang=java
 *
 * [507] 完美数
 */

// @lc code=start
class Solution {
    public boolean checkPerfectNumber(int num) {
        if (num == 6) return true;
        if (num == 28) return true;
        if (num == 496) return true;
        if (num == 8128) return true;
        if (num == 33_550_336) return true;
        return false;
        
        // Set<Integer> set = new HashSet<>();
        // for (int i = 1; i < num; i++) {
        //     if (num % i == 0) set.add(i);
        // }

        // int sum = 0;
        // for (int n: set) {
        //     sum += n;
        // }

        // return sum == num;
    }
}
// @lc code=end

