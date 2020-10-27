import java.util.Set;

/*
 * @lc app=leetcode.cn id=475 lang=java
 *
 * [475] 供暖器
 */

// @lc code=start
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int ans = 0;
        for (int ho: houses) {
            int min = Integer.MAX_VALUE;
            for (int he: heaters) {
                min = Math.min(min, Math.abs(ho-he));
            }
            ans = Math.max(ans, min);
        }
        return ans;
    }
}
// @lc code=end

