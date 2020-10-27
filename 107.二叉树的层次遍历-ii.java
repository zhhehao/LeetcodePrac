import java.util.LinkedList;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=107 lang=java
 *
 * [107] 二叉树的层次遍历 II
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            List<Integer> tmp = new LinkedList<>();
            int len = q.size(); // 每一层的节点数量
            for (int i = 0; i < len; i++) {
                TreeNode node = q.poll();
                tmp.add(node.val); // 每一层所有节点的值都从左至右加入同一个List
                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
            }
            ans.add(0, tmp);
        }
        return ans;






        // List<List<Integer>> ans = new LinkedList<List<Integer>>();
        // if (root == null) return ans;

        // LinkedList<TreeNode> queue = new LinkedList<>();
        // queue.add(root);

        // List<Integer> tl = new LinkedList<>();
        // tl.add(root.val);
        // ans.add(tl);
        
        // while (!queue.isEmpty()) {
        //     TreeNode temp = queue.poll();
        //     if (temp.left == null && temp.right == null) continue;
        //     List<Integer> ll = new LinkedList<>();
        //     if (temp.left != null) {ll.add(temp.left.val); queue.add(temp.left);}
        //     if (temp.right != null) {ll.add(temp.right.val); queue.add(temp.right);}
        //     ans.add(ll);
        // }
        
        // Collections.reverse(ans);

        // return ans;
    }
}
// @lc code=end

