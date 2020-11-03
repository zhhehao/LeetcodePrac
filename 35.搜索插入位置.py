#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left, right, ans = 0, size - 1, size
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

# @lc code=end

