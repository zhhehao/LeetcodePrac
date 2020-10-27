/*
 * @lc app=leetcode.cn id=28 lang=java
 *
 * [28] 实现 strStr()
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) return 0;
        if (needle.length() > haystack.length()) return -1;
        if (needle.length() == haystack.length()) {
            for (int i = 0; i < needle.length(); i++) {
                if (needle.charAt(i) != haystack.charAt(i)) 
                    return -1;
            }
            return 0;
        }


        for (int i = 0; i + needle.length() <= haystack.length(); i++) {
            if (needle.charAt(0) != haystack.charAt(i)) continue;
            boolean findIt = true;
            for (int j = 1; j < needle.length(); j++) {
                if (needle.charAt(j) != haystack.charAt(i+j)) {
                    findIt = false;
                    break;
                }
            }
            if (findIt)
                return i;
        }
        return -1;
    }
}
// @lc code=end

