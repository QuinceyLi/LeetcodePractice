#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        p = t = head
        while p:
            res.append(p.val)
            p = p.next
        res.sort()
        for r in res:
            t.val = r
            t = t.next
        return head
# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

