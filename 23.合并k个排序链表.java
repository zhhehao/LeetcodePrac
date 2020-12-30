import java.util.PriorityQueue;

/*
 * @lc app=leetcode.cn id=23 lang=java
 *
 * [23] 合并K个排序链表
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
    public ListNode mergeKLists(ListNode[] lists) {
        // 优先队列
        // class Node {
        //     ListNode L;
        //     int i;
        //     Node(ListNode L, int i){
        //         this.L = L;
        //         this.i = i;
        //     }
        // }


        // class NodeComparator implements Comparator<Node> {
        //     @Override
        //     public int compare(Node n1, Node n2) {
        //         return n1.L.val - n2.L.val;
        //     }
        // }

        // ListNode ans = null, cur = null;
        // while (true) {
        //     PriorityQueue<Node> q = new PriorityQueue<>(new NodeComparator());
        //     for (int i = 0; i < lists.length; i++) {
        //         if (lists[i] == null) continue;
        //         q.add(new Node(lists[i], i));
        //     }
        //     if (q.size() == 0) break;
        //     if (ans == null) {
        //         Node temp = q.peek();
        //         ans = temp.L;
        //         cur = temp.L;
        //         lists[temp.i] = lists[temp.i].next;
        //     } else {
        //         Node temp = q.peek();
        //         cur.next = temp.L;
        //         cur = temp.L;
        //         lists[temp.i] = lists[temp.i].next;
        //     }
        // }

        // return ans;

        // 分治
        if (lists.length == 0) return null;
        while (lists.length != 1) {
            int len = lists.length;
            if (len % 2 == 1) {
                lists[0] = mergeTwoLists(lists[0], lists[lists.length-1]);
                len = lists.length - 1;
            }
            
            ListNode[] newLists = new ListNode[len / 2];
            int j = 0;
            for (int i = 0; i < len; i += 2) {
                newLists[j++] = mergeTwoLists(lists[i], lists[i+1]);
            }
            lists = newLists;
        }

        return lists[0];


        // 顺序合并
        // ListNode ans = null, cur = null;
        // while (!isAllNull(lists)) {
        //     int i = 0;
        //     while (lists[i] == null) i++;
        //     int minL = i;
        //     i++;
        //     while (i < lists.length) {
        //         if (lists[i] != null && lists[i].val < lists[minL].val) {
        //             minL = i;
        //         } 
        //         i++;
        //     }
        //     if (ans == null) {
        //         ans = lists[minL];
        //         cur = ans;
        //         lists[minL] = lists[minL].next;
        //     } else {
        //         cur.next = lists[minL];
        //         cur = lists[minL];
        //         lists[minL] = lists[minL].next;
        //     }
            
        // }

        // return ans;
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode ans, cur;
        if (l1.val <= l2.val) {
            ans = l1;
            cur = l1;
            l1 = l1.next;
        } else {
            ans = l2;
            cur = l2;
            l2 = l2.next;
        }

        while (l1 != null || l2 != null) {
            if (l1 == null) {
                cur.next = l2;
                break;
            } else if (l2 == null) {
                cur.next = l1;
                break;
            } else {
                if (l1.val <= l2.val) {
                    cur.next = l1;
                    cur = l1;
                    l1 = l1.next;
                } else {
                    cur.next = l2;
                    cur = l2;
                    l2 = l2.next;
                }
            }
        }

        return ans;
    }

    private boolean isAllNull(ListNode[] lists) {
        for (ListNode ln : lists) {
            if (ln != null) return false;
        }
        return true;
    }

}
// @lc code=end

