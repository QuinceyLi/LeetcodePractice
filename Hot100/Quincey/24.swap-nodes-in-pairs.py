# @lcpr-before-debug-begin
from python3problem24 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        t1, t2, head = head, head.next, head.next
        temp = ListNode() # 用来连接各部分
        while t1 and t2:
            t1.next,t2.next = t2.next, t1
            temp.next = t2 # temp指向交换完之后的第一个

            # 保证t1,t2先后顺序,temp是交换完之后靠后的指针
            temp,t1 = t1,t2 
            t2 = temp

            t1 = t1.next.next
            if t1:
                t2 = t2.next.next
            else:
                return head
        return head
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

