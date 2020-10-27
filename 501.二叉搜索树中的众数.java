import java.util.ArrayList;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=501 lang=java
 *
 * [501] 二叉搜索树中的众数
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> map = new HashMap<>();
        viewTree(map, root);
        int max = findMaxValue(map);

        ArrayList<Integer> arr = new ArrayList<>();
        for (int k: map.keySet()) {
            if (map.get(k) == max) arr.add(k);
        }

        int[] ans = new int[arr.size()];
        
        int i = 0;
        for (int a: arr) {
            ans[i++] = a;
        }
        return ans;
    }

    private void viewTree(Map<Integer, Integer> map, TreeNode root) {
        if (root == null) return;
        if (map.containsKey(root.val)) {
            map.put(root.val, map.get(root.val)+1);
        } else {
            map.put(root.val, 1);
        }
        viewTree(map, root.left);
        viewTree(map, root.right);
    }

    private int findMaxValue(Map<Integer, Integer> map) {
        int max = 0;
        for (int v: map.values()) {
            max = Math.max(max, v);
        }
        return max;
    }
}
// @lc code=end

