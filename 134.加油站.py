#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 多次遍历
        # n = len(gas)
        
        # def solve(i):
        #     step = n
        #     oil = 0
        #     cur = i
        #     while step > 0:
        #         next = cur + 1 if cur + 1 < n else 0
        #         oil += gas[cur]
        #         if oil < cost[cur]:
        #             return False
        #         oil -= cost[cur]
        #         step -= 1
        #         cur = next
        #     return True

        # for i in range(n):
        #     if solve(i):
        #         return i

        # return -1

        # 一次遍历
        n = len(gas)
        i = 0
        while i < n:
            sumOfGas, sumOfCost = 0, 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sumOfGas += gas[j]
                sumOfCost += cost[j]
                if sumOfCost > sumOfGas:
                    break
                cnt += 1
            if cnt == n:
                return i
            else:
                i = i + cnt + 1

        return -1





# @lc code=end

