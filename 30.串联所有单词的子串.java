/*
 * @lc app=leetcode.cn id=30 lang=java
 *
 * [30] 串联所有单词的子串
 */

// @lc code=start
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<>();
        if (s.length() == 0) return ans;
        if (words.length == 0) return ans;
        int len = words.length * words[0].length();
        
        Arrays.sort(words);
        for (int i = 0; i+len <= s.length(); i++) {
            if (isMatch(s.substring(i, i+len), words)) ans.add(i);
        }
        return ans;
    }

    private boolean isMatch(String s, String[] words) {
        int len = words[0].length();
        String[] strs = new String[words.length];
        int j = 0;
        for (int i = 0; i + len <= s.length(); i += len) {
            strs[j++] = s.substring(i, i+len);
        }
        Arrays.sort(strs);
        for (int i = 0; i < words.length; i++) {
            if (!words[i].equals(strs[i])) return false;
        }
        return true;
    }
}
// @lc code=end

