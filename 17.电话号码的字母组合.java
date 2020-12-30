/*
 * @lc app=leetcode.cn id=17 lang=java
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return new ArrayList<String>();
        }
        List<String> ans = new ArrayList<>();
        String[] tel = new String[10];
        tel[2] = "abc";
        tel[3] = "def";
        tel[4] = "ghi";
        tel[5] = "jkl";
        tel[6] = "mno";
        tel[7] = "pqrs";
        tel[8] = "tuv";
        tel[9] = "wxyz";

        getComb(ans, digits, 1, tel, "");
        return ans;
    }

    private void getComb(List<String> ans, String digits, int level, String[] tel, String s) {
        if (level == digits.length()) {
            int n = digits.charAt(level-1)-'0';
            for (char c: tel[n].toCharArray()) {
                ans.add(s + c);
            }
            return;
        }
        int n = digits.charAt(level-1)-'0';
        for (char c: tel[n].toCharArray()) {
            getComb(ans, digits, level+1, tel, s+c);
        }
    }
}
// @lc code=end

