#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        # n = len(nums)
        # ans = []

        # def solve(rec, st):
        #     ans.append(list(rec))
        #     for i in range(st, n):
        #         rec.append(nums[i])
        #         solve(rec, i+1)
        #         rec.pop()
        
        # solve([], 0)
        # return ans

        # 掩码法
        n = len(nums)
        ans = []
        max_mask = 1 << n
        for mask in range(max_mask):
            rec = []
            for i in range(n):
                if mask &(1 << i) != 0:
                    rec.append(nums[i])
            ans.append(list(rec))

        return ans

# @lc code=end

