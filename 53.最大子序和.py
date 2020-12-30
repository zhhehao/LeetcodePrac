#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # # DP
        # n = len(nums)
        # dp =[0] * n
        # dp[0] = nums[0]
        # ans = dp[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1] + nums[i], nums[i])
        #     ans = max(ans, dp[i])

        # return ans

        # 分治

        class Status:
            def __init__(self, lSum, rSum, mSum, iSum) -> None:            
                self.lSum = lSum
                self.rSum = rSum
                self.mSum = mSum
                self.iSum = iSum

        def getInfo(l, r):
            if l == r:
                return Status(nums[l], nums[l], nums[l], nums[l])
            m = (l + r) >> 1
            lSub = getInfo(l, m)
            rSub = getInfo(m+1, r)
            return pushUp(lSub, rSub)

        def pushUp(l, r):
            iSum = l.iSum + r.iSum
            lSum = max(l.lSum, l.iSum + r.lSum)
            rSum = max(r.rSum, r.iSum + l.rSum)
            mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum)
            return Status(lSum, rSum, mSum, iSum)

        return getInfo(0, len(nums)-1).mSum
# @lc code=end

