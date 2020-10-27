import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=104 lang=java
 *
 * [104] 二叉树的最大深度
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
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        LinkedList<Node> stack = new LinkedList<>();
        stack.push(new Node(root, 1));
        int depth = 1;

        while (!stack.isEmpty()) {
            Node temp = stack.pop();
            if (temp.depth > depth) depth = temp.depth;
            if (temp.node.left != null)
                stack.push(new Node(temp.node.left, temp.depth+1));
            if (temp.node.right != null)
                stack.push(new Node(temp.node.right, temp.depth+1));
        }

        return depth;
    }
}

class Node {
    Node(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
    int depth;
    TreeNode node;
}
// @lc code=end

