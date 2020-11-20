#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        idx = 0
        for s in strs:
            l = list(s)
            l.sort()
            s_sorted = str(l)
            if s_sorted in d:
                ans[d[s_sorted]].append(s)
            else:
                ans.append([s])
                d[s_sorted] = idx
                idx += 1

        return ans
# @lc code=end

