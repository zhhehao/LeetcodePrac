# @before-stub-for-debug-begin
from python3problem55 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, p = len(nums), 0
        for i in range(n):
            if i <= p:
                p = max(p, i+nums[i])
                if p >= n-1:
                    return True
        return False

# @lc code=end

