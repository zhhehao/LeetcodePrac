/*
 * @lc app=leetcode.cn id=412 lang=java
 *
 * [412] Fizz Buzz
 */

// @lc code=start
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            String s = "";

            if (i % 3 == 0) {
                s += "Fizz";
            }
            if (i % 5 == 0) {
                s += "Buzz";
            } 
            if (s == "") {
                s += i;
            }

            ans.add(s);
        }
        return ans;
    }
}
// @lc code=end

