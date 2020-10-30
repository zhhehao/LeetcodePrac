#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_nums(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        flag = False
        size = len(nums)
        for i in range(size-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = size - 1
                while j > i:
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
                    j -= 1
                if j == i:
                   nums[i], nums[i-1] = nums[i-1], nums[i]
                reverse_nums(i, size-1)             
                flag = True
                break
        
        if not flag:
            reverse_nums(0, size - 1)
# @lc code=end

