#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        size = len(nums)

        left, right = 0, size - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                start = end = mid
                while start >= 0 and nums[start] == target:
                    start -= 1
                while end < size and nums[end] == target:
                    end += 1
                return [start + 1, end - 1]
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1


        return [-1, -1]
# @lc code=end

