/*
 * @lc app=leetcode.cn id=409 lang=java
 *
 * [409] 最长回文串
 */

// @lc code=start
class Solution {
    public int longestPalindrome(String s) {
        int[] c1 = new int[26];
        int[] c2 = new int[26];

        for (char c : s.toCharArray()) {
            if (Character.isLowerCase(c)) c1[c-'a']++;
            else c2[c-'A']++;
        }

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (c1[i] % 2 == 0) ans += c1[i];
            else if (c1[i] != 0) ans += (c1[i]-1);
            if (c2[i] % 2 == 0) ans += c2[i];
            else if (c2[i] != 0) ans += (c2[i]-1);
        }

        if (ans < s.length()) return ans + 1;
        else return ans;
    }
}
// @lc code=end

