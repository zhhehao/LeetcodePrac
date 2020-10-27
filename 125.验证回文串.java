/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {

        int i = 0, j = s.length()-1;
        while (i < j) {
            while (!Character.isLetterOrDigit(s.charAt(i)) && i < j) i++;
            while (!Character.isLetterOrDigit(s.charAt(j)) && i < j) j--;
            if (Character.isDigit(s.charAt(i)) && s.charAt(i) != s.charAt(j)) return false;
            if (Character.isLetter(s.charAt(i))) {
                if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j)))
                    return false;
            } 
            i++;
            j--;
        }
        return true;
    }
}
// @lc code=end

