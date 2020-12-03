#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        if n == 1:
            return '/'
        new_path = ['/']

        i = 1
        while i < n:
            while i < n and path[i] == '/':
                i += 1
            if i == n:
                break
            start = i
            while i < n and path[i] != '/':
                i += 1
            end = i
            d = path[start:end]
            if d == '.':
                continue
            elif d == '..':
                if new_path[-1] != '/':
                    new_path.pop()
            else:
                new_path.append(d)            

        rec = ''
        for d in new_path[1:]:
            rec = rec + '/' + d
        if len(rec) == 0:
            return '/'
        return rec
        
    # @lc code=end

