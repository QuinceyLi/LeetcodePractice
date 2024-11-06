#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head:
        #     return False
        # p1 = head
        # while p1.next:
        #     p2 = p1
        #     p1 = p1.next
        #     if p1 == p2:
        #         return True
        #     temp = head
        #     while temp != p2:
        #         if temp == p1:
        #             return True
        #         else:
        #             temp = temp.next
        # return False
        slow = fast = head  # 乌龟和兔子同时从起点出发
        while fast and fast.next:
            slow = slow.next  # 乌龟走一步
            fast = fast.next.next  # 兔子走两步
            if fast is slow:  # 兔子追上乌龟（套圈），说明有环
                return True
        return False  # 访问到了链表末尾，无环
                
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

