#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        ans = []
        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = size - 1
            target = -nums[i]
            for j in range(i+1, size):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans
# @lc code=end

