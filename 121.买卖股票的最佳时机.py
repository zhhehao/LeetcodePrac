#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 双重循环，超时
        # rec = 0
        # n = len(prices)
        # for i in range(n-1):
        #     for j in range(i, n):
        #         rec = max(rec, prices[j]-prices[i])
        # return rec

        n = len(prices)
        if n < 2:
            return 0
        i, j = 0, 1
        rec = 0
        while j < n:
            if prices[j] >= prices[i]:
                rec = max(rec, prices[j]-prices[i])
                j += 1
            else:
                i = j
                j = i+1

        return rec



# @lc code=end

