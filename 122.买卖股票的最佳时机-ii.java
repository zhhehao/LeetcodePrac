/*
 * @lc app=leetcode.cn id=122 lang=java
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        for (int i = 0; i < prices.length-1; i++) {
            if (prices[i] < prices[i+1]) 
                ans += (prices[i+1]-prices[i]);
        }
        return ans;


        // if (prices.length < 2) return 0;
        // if (prices.length == 2) {
        //     return Math.max(0, prices[1]-prices[0]);
        // }
        // int bp = 0, sp = 0;
        // int ans = 0;
        // int i = 0;
        
        // while (i < prices.length) {
        //     int bpi = getBP(prices, i, prices.length-1);
        //     bp = prices[bpi];
        //     i = bpi + 1;
        //     int spi = getSP(prices, i, prices.length-1);
        //     sp = prices[spi];
        //     if (sp < bp) break;
        //     ans += (sp-bp);
        //     i = spi + 1;
        // }

        // return ans;
    }

    private int getBP(int[] prices, int start, int end) {
        while (start < end-1) {
            if (prices[start] < prices[start+1]) {
                return start;
            }
            start++;
        }
        return end-1;
    }

    private int getSP(int[] prices, int start, int end) {
        while (start < end) {
            if (prices[start] > prices[start+1]) {
                return start;
            }
            start++;
        }
        return end;
    }
}
// @lc code=end

