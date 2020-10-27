/*
 * @lc app=leetcode.cn id=459 lang=java
 *
 * [459] 重复的子字符串
 */

// @lc code=start
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        for (int i = 2; i <= s.length(); i++) {
            if (s.length() % i != 0) continue;
            if (isRepeated(s, s.length()/i)) return true;
        }
        return false;
    }

    private boolean isRepeated(String s, int d) {
        String s1 = s.substring(0, d);
        int j = d;
        while (j < s.length()) {
            if (!s.substring(j, j+d).equals(s1)) return false;
            j += d;
        }
        return true;
    }
}
// @lc code=end

