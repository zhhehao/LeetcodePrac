/*
 * @lc app=leetcode.cn id=25 lang=java
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode nextHead = head;
        for (int i = 0; i < k; i++) {
            if (nextHead == null) return head;
            nextHead = nextHead.next;
        }

        ListNode next = reverseKGroup(nextHead, k);
        ListNode cur = head;
        for (int i = 0; i < k; i++) {
            ListNode temp = cur;
            cur = cur.next;
            temp.next = next;
            next = temp;
        }

        return next;
    }
}
// @lc code=end

