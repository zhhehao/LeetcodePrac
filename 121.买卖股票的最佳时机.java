/*
 * @lc app=leetcode.cn id=121 lang=java
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) return 0;
        
        int lo = prices[0];
        int ans = Math.max(0, prices[1]-lo);

        for (int i = 2; i < prices.length; i++) {
            if (prices[i-1] < lo)
                lo = prices[i-1];
            ans = Math.max(ans, prices[i]-lo);
        }


        return ans;
    }
}
// @lc code=end

