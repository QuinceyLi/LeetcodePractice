# @lcpr-before-debug-begin
from python3problem19 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = temp2 = head
        for i in range(n): 
            if temp2.next:
                temp2 = temp2.next
            else:
                return head.next
        while temp2.next:          
            temp = temp.next
            temp2 = temp2.next
        temp.next = temp.next.next
        return head
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

