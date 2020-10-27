import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=83 lang=java
 *
 * [83] 删除排序链表中的重复元素
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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode p = head;

        while (p != null && p.next != null) {
            if (p.val == p.next.val) {
                p.next = p.next.next;
            } else {
                p = p.next;
            }
        }


        return head;



        // if (head == null) return null;
        // HashSet<Integer> hs = new HashSet<>();
        // ListNode rev = head;
        // ListNode p = rev;
        // hs.add(head.val);
        // head = head.next;
 
        // while(head != null) {
        //     if (!hs.contains(head.val)) {
        //         hs.add(head.val);
        //         p.next = head;
        //         p = p.next;
        //     }
        //     head = head.next;
        // }
        // p.next = null;
        // return rev;
    }
}
// @lc code=end

