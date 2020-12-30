# @before-stub-for-debug-begin
from python3problem81 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def b_search(l, r):
            if l == r:
                return True if nums[l] == target else False

            if r < l:
                return False


            m = (l + r) // 2
            # print('l is ', l, 'r is ', r, 'm is ', m)
            if nums[m] == target:
                return True

            if m-1 >= l and nums[l] < nums[m-1]:
                nl = l
                nr = m-1
                while nl <= nr:
                    mid = (nl + nr) // 2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        nl = mid + 1
                    else:
                        nr = mid - 1

            if m+1 <= r and nums[m+1] < nums[r]:
                nl = m+1
                nr = r
                while nl <= nr:
                    mid = (nl + nr) // 2
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        nl = mid + 1
                    else:
                        nr = mid - 1
                      

            if b_search(l, m-1):
                return True

            if b_search(m+1, r):
                return True

            return False

        n = len(nums)
        return False if n == 0 else b_search(0, n-1)

            
# @lc code=end

