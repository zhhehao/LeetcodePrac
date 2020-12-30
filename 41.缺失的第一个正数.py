# @before-stub-for-debug-begin
from python3problem41 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 哈希表
        # size = len(nums)
        # for i in range(size):
        #     if nums[i] <= 0:
        #         nums[i] = size + 1
        
        # for i in range(size):
        #     num = abs(nums[i])
        #     if num <= size:
        #         nums[num-1] = -abs(nums[num-1])

        # for i in range(size):
        #     if nums[i] > 0:
        #         return i + 1


        # return size + 1

        # 置换
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1 
            


# @lc code=end

