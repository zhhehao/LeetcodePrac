#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def format_words(line, isLastLine=False):
            rec = ""
            if isLastLine:
                for w in line:
                    rec = rec + w + ' '
                if len(rec) > maxWidth:
                    return rec[0:-1]
                else:
                    return rec + (' ' * (maxWidth-len(rec)))
            else:
                words_len = 0
                for i in range(len(line)):
                    words_len += len(line[i])
                space_len = maxWidth - words_len
                space_cnt = len(line) - 1                
                space_even = space_len // space_cnt
                space = [space_even] * space_cnt
                space_left = space_len - space_even * space_cnt
                i = 0
                while space_left > 0:
                    space[i] += 1
                    space_left -= 1
                    i += 1
                space.append(0)
                for i in range(len(line)):
                    rec = rec + line[i] + ' ' * space[i]
                return rec


        i, n = 0, len(words)
        ans = []

        while i < n:
            start, end = i, i
            length = maxWidth - len(words[i])
            i += 1
            while i < n and len(words[i]) + 1 <= length:
                end += 1
                length -= len(words[i]) + 1
                i += 1
            isLastLine = (i == n) or (start == end)
            ans.append(format_words(words[start:end+1], isLastLine))

        return ans



# @lc code=end

