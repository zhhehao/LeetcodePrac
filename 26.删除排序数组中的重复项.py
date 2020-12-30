#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0

        # v = nums[0]
        # i = 1
        # p = 1
        # size = len(nums)

        # while i < size:
        #     if nums[i] == v:
        #         i += 1
        #         continue
        #     nums[p] = nums[i]
        #     v = nums[i]
        #     i += 1
        #     p += 1

        # return p
        
        if not nums:
            return 0
        i = 0
        size = len(nums)
        for j in range(1, size):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

# @lc code=end

