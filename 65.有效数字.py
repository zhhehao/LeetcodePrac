#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        space_states = (0, -1, 9, 9, -1, 9, -1, -1, 9, 9)
        sign_states = (1, -1, -1, -1, 6, -1, -1, -1, -1, -1)
        number_states = (2, 2, 2, 3, 5, 5, 5, 8, 8, -1)
        dot_states = (7, 7, 3, -1, -1, -1, -1, -1, -1, -1)
        e_states = (-1, -1, 4, 4, -1, -1, -1, -1, 4, -1)
        states = (space_states, sign_states, number_states, dot_states, e_states)

        state = 0

        for c in s:
            if state < 0:
                return False
            if c == ' ':
                state = states[0][state]
            elif c in ('+', '-'):
                state = states[1][state]
            elif c.isdigit():
                state = states[2][state]
            elif c == '.':
                state = states[3][state]
            elif c == 'e':
                state = states[4][state]
            else:
                state = -1

        return True if state in (2, 3, 5, 8, 9) else False

            


# @lc code=end

