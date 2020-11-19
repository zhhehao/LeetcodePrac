#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        flag = [False] * size
        ans = []

        def solve(rec, cnt):
            if cnt == size:
                ans.append(rec[:])
                return
            
            for i in range(size):
                if flag[i]:
                    continue
                flag[i] = True
                rec.append(nums[i])
                solve(rec, cnt+1)
                rec.pop()
                flag[i] = False
        
        solve([], 0)
        return ans

# @lc code=end

