#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)-1
        i, rec, buy_in = 0, 0, -1
        while i < n:
            if buy_in == -1 and prices[i+1] > prices[i]:
                buy_in = prices[i]
            elif buy_in != -1 and prices[i+1] < prices[i]:
                rec += (prices[i]-buy_in)
                buy_in = -1
            i += 1
        return rec if buy_in == -1 else rec + prices[n] - buy_in

        
# @lc code=end

