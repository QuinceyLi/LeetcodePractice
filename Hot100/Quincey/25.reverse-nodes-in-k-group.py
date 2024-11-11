# @lcpr-before-debug-begin
from python3problem25 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # t1,flag,con = head, 0, head
        # while t1:
        #     t2 = t1
        #     for i in range(k-1):
        #         if t2.next: t2 = t2.next
        #         else: break
        #     if i < k-1:break
        #     else:
        #         if 
        #             con.next = t2
        #         for i in range(k-1):
        #             t2, temp, t2.next = temp, t2.next, t1
        #             t1 = t2  
        #         t1 = temp
        #         flag += 1
        # return head
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head

        # k 个一组处理
        while n >= k:
            n -= k
            for _ in range(k):  # 同 92 题
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            # 见视频
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

