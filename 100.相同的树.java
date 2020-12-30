import java.util.LinkedList;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=100 lang=java
 *
 * [100] 相同的树
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null && q != null) return false;
        if (p != null && q == null) return false;

        LinkedList<TreeNode> s1 = new LinkedList<>();
        LinkedList<TreeNode> s2 = new LinkedList<>();

        while (p != null|| !s1.isEmpty()) {
            if (p != null) {
                if (p.val != q.val) return false;
                s1.push(p);
                s2.push(q);
                p = p.left;
                q = q.left;
                if (p == null && q != null) return false;
                if (p != null && q == null) return false;
            } else {
                TreeNode p1 = s1.pop();
                TreeNode p2 = s2.pop();
                p = p1.right;
                q = p2.right;
                if (p == null && q != null) return false;
                if (p != null && q == null) return false;
            }
        }
        if (q != null || !s2.isEmpty()) return false;

        return true;
    }
}
// @lc code=end

