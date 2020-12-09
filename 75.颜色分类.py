#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 单指针
        # n = len(nums)
        # p = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         nums[p], nums[i] = nums[i], nums[p]
        #         p += 1
        # for i in range(p, n):
        #     if nums[i] == 1:
        #         nums[p], nums[i] = nums[i], nums[p]
        #         p += 1

        # 双指针
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1

        # @lc code=end

