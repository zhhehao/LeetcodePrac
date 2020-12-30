/*
 * @lc app=leetcode.cn id=455 lang=java
 *
 * [455] 分发饼干
 */

// @lc code=start
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0, j = 0;
        int ans = 0;
        while (i < g.length && j < s.length) {
            while (j < s.length && s[j] < g[i]) j++;
            if (j == s.length) break;
            ans++;
            i++;
            j++;
        }
        return ans;
    }
}
// @lc code=end

