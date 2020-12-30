/*
 * @lc app=leetcode.cn id=32 lang=java
 *
 * [32] 最长有效括号
 */

// @lc code=start
class Solution {
    public int longestValidParentheses(String s) {
        // left right
        int left = 0, right = 0, ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                ans = Math.max(ans, 2 * right);
            } else if (right >= left) {
                left = right = 0;
            }
        }

        left = right = 0;
        for (int i = s.length()-1; i>= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                ans = Math.max(ans, 2 * left);
            } else if (left >= right) {
                left = right = 0;
            }
        }
        return ans;

        // stack
        // int ans = 0;
        // Stack<Integer> stack = new Stack<>();
        // stack.push(-1);
        // for (int i = 0; i < s.length(); i++) {
        //     if (s.charAt(i) == '(') {
        //         stack.push(i);
        //     } else {
        //         stack.pop();
        //         if (stack.empty()) stack.push(i);
        //         else ans = Math.max(ans, i-stack.peek());
        //     }
        // }
        // return ans;

        // DP
        // int ans = 0;
        // int[] dp = new int[s.length()];
        // for (int i = 1; i < s.length(); i++) {
        //     if (s.charAt(i) == ')') {
        //         if (s.charAt(i-1) == '(') {
        //             dp[i] = (i >= 2 ? dp[i-2] : 0) + 2;
        //         } else if (i-dp[i-1] > 0 && s.charAt(i-dp[i-1]-1) == '(') {
        //             dp[i] = dp[i-1] + ((i-dp[i-1]) >= 2 ? dp[i-dp[i-1]-2] : 0) + 2;
        //         }
        //         ans = Math.max(ans, dp[i]);
        //     }
        // }
        // return ans;
    }
}
// @lc code=end

