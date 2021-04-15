#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 两次遍历
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
            else:
                left[i] = 1

        right = ret = 0
        for i in range(n-1, -1, -1):
            if i < n-1 and ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret

        
# @lc code=end

