import java.util.Set;

/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        int head = 0, tail = 1, ans = 0;
        Set<Character> set = new HashSet<>();
        set.add(s.charAt(head));
        ans = set.size();

        for (; tail < s.length(); tail++) {
            char c = s.charAt(tail);
            if (!set.contains(c)) {
                set.add(c);
                ans = Math.max(ans, tail-head);
            } else {
                ans = Math.max(ans, tail-head);
                while (true) {
                    char c2 = s.charAt(head);
                    if (c2 == c) {
                        head++;
                        break;
                    } else {
                        set.remove(c2);
                        head++;
                    }
                }
            }
        }
        ans = Math.max(ans, tail-head);
        return ans;
        
    }
}
// @lc code=end

