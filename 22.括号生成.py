#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = list()

        def genPar(s, left, right):
            if not left and not right:
                ans.append(s)
                return
            if left:
                s += '('
                genPar(s, left-1, right)
                s = s[:-1]
            if right > left:
                s += ')'
                genPar(s, left, right-1)
                s = s[:-1]

        genPar('', n, n)
        return ans

# @lc code=end

