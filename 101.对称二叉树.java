/*
 * @lc app=leetcode.cn id=101 lang=java
 *
 * [101] 对称二叉树
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
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);

        // if (root == null) return true;
        // TreeNode p = root, q = root;

        // LinkedList<TreeNode> s1 = new LinkedList<>();
        // LinkedList<TreeNode> s2 = new LinkedList<>();

        // while (p != null|| !s1.isEmpty()) {
        //     if (p != null) {
        //         if (p.val != q.val) return false;
        //         s1.push(p);
        //         s2.push(q);
        //         p = p.left;
        //         q = q.right;
        //         if (p == null && q != null) return false;
        //         if (p != null && q == null) return false;
        //     } else {
        //         TreeNode p1 = s1.pop();
        //         TreeNode p2 = s2.pop();
        //         p = p1.right;
        //         q = p2.left;
        //         if (p == null && q != null) return false;
        //         if (p != null && q == null) return false;
        //     }
        // }
        // if (q != null || !s2.isEmpty()) return false;

        // return true;
    }

    private boolean isMirror(TreeNode r1, TreeNode r2) {
        if (r1 == null && r2 == null) return true;
        if (r1 == null || r2 == null) return false;
        return (r1.val == r2.val) &&
            isMirror(r1.left, r2.right) &&
            isMirror(r1.right, r2.left);
    }
}
// @lc code=end

