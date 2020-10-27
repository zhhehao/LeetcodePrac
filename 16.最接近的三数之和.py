#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        ans = 10 ** 7

        for i in range(size):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, size - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s > target:
                    new_k = k - 1
                    while new_k > j and nums[new_k] == nums[k]:
                        new_k -= 1
                    k = new_k
                else:
                    new_j = j + 1
                    while new_j < k and nums[new_j] == nums[j]:
                        new_j += 1
                    j = new_j
                
        return ans

# @lc code=end

