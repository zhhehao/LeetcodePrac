/*
 * @lc app=leetcode.cn id=119 lang=java
 *
 * [119] 杨辉三角 II
 */

// @lc code=start
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<integer>[] ans = new List<integer>[34];
        List<Integer> rev = new LinkedList<>();
        rev.add(1);
        ans.add(rev);
        rev.add(1);
        ans.add(rev);
        if (rowIndex == 0) return ans.get(0);
        if (rowIndex == 1) return ans.get(1);
        if (ans.size() > )
        for (int i = 2; i <= rowIndex; i++) {
            for (int j = 0; j < rev.size()-1; j++) {
                rev.set(j, rev.get(j)+rev.get(j+1));
            }
            rev.add(0,1);
        }
        return rev;
    }        
}
// @lc code=end

