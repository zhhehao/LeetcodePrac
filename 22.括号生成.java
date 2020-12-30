import java.util.List;

/*
 * @lc app=leetcode.cn id=22 lang=java
 *
 * [22] 括号生成
 */

// @lc code=start
class Solution {
    ArrayList[] cache = new ArrayList[100];

    public List<String> generateParenthesis(int n) {
        // 按括号序列的长度递归
        return generate(n);

        // 回溯法
        // List<String> ans = new ArrayList<>();
        // genePare(ans, new StringBuilder(), 0, 0, n);
        // return ans;
    }

    private List<String> generate(int n) {
        if (cache[n] != null) return cache[n];
        ArrayList<String> ans = new ArrayList<>();
        if (n == 0) {
            ans.add("");
        } else {
            for (int c = 0; c < n; ++c) {
                for (String left: generate(c)) {
                    for (String right: generate(n-1-c))
                        ans.add("(" + left + ")" + right);
                }
            }
        }
        cache[n] = ans;
        return ans;
    }

    private void genePare(List<String> ans, StringBuilder cur, int open, int close, int max) {
        if (cur.length() == max * 2) {
            ans.add(cur.toString());
            return;
        }
        
        if (open < max) {
            cur.append('(');
            genePare(ans, cur, open+1, close, max);
            cur.deleteCharAt(cur.length()-1);
        }

        if (close < open) {
            cur.append(')');
            genePare(ans, cur, open, close+1, max);
            cur.deleteCharAt(cur.length()-1);
        }
    }
}
// @lc code=end

