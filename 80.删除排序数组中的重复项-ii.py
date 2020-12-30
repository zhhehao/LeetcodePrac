#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len (nums)
        p = 1
        second = True
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                if second:
                    nums[p] = nums[i]
                    p += 1
                    second = False
            else:
                second = True
                nums[p] = nums[i]
                p += 1

        return p
# @lc code=end

