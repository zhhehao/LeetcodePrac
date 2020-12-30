import java.util.ArrayDeque;

/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        int[] mark = new int[nums.length];
        ArrayDeque<Integer> path = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            mark[i] = 1;
            path.addLast(nums[i]);
            returnPermute(nums, mark, path, nums.length-1, ans);
            path.removeLast();
            mark[i] = 0;
        }
        return ans;
    }

    private void returnPermute(int[] nums, 
                                        int[] mark, 
                                        ArrayDeque<Integer> path, 
                                        int steps,
                                        List<List<Integer>> ans) {
        if (steps == 0) {
            ans.add(new ArrayList<Integer>(path));
            return;
        }               
        
        for (int i = 0; i < nums.length; i++) {
            if (mark[i] == 1) continue;
            mark[i] = 1;
            path.addLast(nums[i]);
            returnPermute(nums, mark, path, steps - 1, ans);
            path.removeLast();
            mark[i] = 0;
        }
    }
}
// @lc code=end

