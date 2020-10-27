/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;

        Stack<Character> st = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                st.push(s.charAt(i));
            } else if (st.empty()) {
                return false;
            } else {
                if (st.peek() == '(' && s.charAt(i) == ')') st.pop();
                else if (st.peek() == '{' && s.charAt(i) == '}') st.pop();
                else if (st.peek() == '[' && s.charAt(i) == ']') st.pop();
                else return false;
            }
        }

        if (st.empty())
            return true;
        else 
            return false;
    }
}
// @lc code=end

