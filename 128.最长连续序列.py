#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        rec = 0

        for num in num_set:
            if num-1 in num_set:
                continue
            cnt = 1
            temp = num
            while temp + 1 in num_set:
                cnt += 1
                temp += 1
            rec = max(rec, cnt)

        return rec

# @lc code=end

