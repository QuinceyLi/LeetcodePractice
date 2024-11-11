# @lcpr-before-debug-begin
from python3problem138 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head:
        #     return
        # newhead = Node(head.val, None, None)
        # temp, temp1 = head, newhead
        # while temp.next:
        #     temp1.next = Node(temp.next.val, None, None)
        #     temp, temp1 = temp.next, temp1.next
        # temp, temp1 = head, newhead
        # while temp:
        #     temp2, temp3 = head, newhead
        #     if temp.random:
        #         while temp2 != temp.random: temp2,temp3 = temp2.next,temp3.next
        #         temp1.random = temp3
        #     temp, temp1 = temp.next, temp1.next
        # return newhead
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


       
# @lc code=end

#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#

