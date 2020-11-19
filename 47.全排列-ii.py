#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # set 去重
        # size = len(nums)
        # flag = [False] * size
        # ans = []
        # pu = set()

        # def solve(rec, cnt):
        #     if cnt == size:
        #         t = tuple(rec)
        #         if t not in pu:
        #             ans.append(rec[:])
        #             pu.add(t)
        #         return
            
        #     for i in range(size):
        #         if flag[i]:
        #             continue
        #         flag[i] = True
        #         rec.append(nums[i])
        #         solve(rec, cnt+1)
        #         rec.pop()
        #         flag[i] = False
        
        # solve([], 0)
        # return ans

        size = len(nums)
        flag = [False] * size
        ans = []
        nums.sort()

        def solve(rec, cnt):
            if cnt == size:
                ans.append(rec[:])
                return
            
            for i in range(size):
                if flag[i] or (i > 0 and nums[i] == nums[i-1] and not flag[i-1]):
                    continue
                flag[i] = True
                rec.append(nums[i])
                solve(rec, cnt+1)
                rec.pop()
                flag[i] = False
        
        solve([], 0)
        return ans

# @lc code=end

