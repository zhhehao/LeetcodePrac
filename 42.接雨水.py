# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 暴力法
        # ans = 0
        # n = len(height)
        # counted = set()
        # for i in range(1, n-1):
        #     if i in counted:
        #         continue
        #     left, right = i, i
        #     while left >= 0 and height[left] <= height[i]:
        #         left -= 1
        #     while right < n and height[right] <= height[i]:
        #         right += 1
        #     if left == i or right == i or left < 0 or right >= n or height[left] <= height[i] or height[right] <= height[i]:
        #         continue
        #     ans += (right-left-1) * (min(height[left], height[right])-height[i])
        #     for j in range(i+1, right):
        #         if height[j] == height[i]:
        #             counted.add(j)
        #     # print(i, left, right, (right-left-1) * (min(height[left], height[right])-height[i]))
        # return ans

        # dp
        # if not height:
        #     return 0
        # ans = 0
        # size = len(height)
        # left_max, right_max = [None] * size, [None] * size
        # left_max[0] = height[0]
        # for i in range(1, size):
        #     left_max[i] = max(height[i], left_max[i-1])
        # right_max[size-1] = height[size-1]
        # for i in range(size-2, -1, -1):
        #     right_max[i] = max(height[i], right_max[i+1])
        # for i in range(1, size-1):
        #     ans += min(left_max[i], right_max[i]) - height[i]
        # return ans

        # stack
        # ans, cur = 0, 0
        # size = len(height)
        # stack = []
        # while cur < size:
        #     while stack and height[cur] > height[stack[-1]]:
        #         top = stack.pop()
        #         if not stack:
        #             break
        #         distance = cur - stack[-1] - 1
        #         bounded_height = min(height[cur], height[stack[-1]]) - height[top]
        #         ans += distance * bounded_height
        #     stack.append(cur)
        #     cur += 1
        # return ans

        # 双指针
        size = len(height)
        left, right = 0, size-1
        ans = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])
                right -= 1

        return ans
# @lc code=end

