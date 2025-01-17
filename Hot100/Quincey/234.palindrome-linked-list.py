# @lcpr-before-debug-begin
from python3problem234 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vallist = []
        temp = head
        while temp:
            vallist.append(temp.val)
            temp = temp.next
        # if vallist == list(reversed(vallist)):
        #     return True
        # else:
        #     return False
        return vallist == vallist[::-1]
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

