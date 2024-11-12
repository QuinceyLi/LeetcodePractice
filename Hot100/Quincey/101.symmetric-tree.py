# @lcpr-before-debug-begin
from python3problem101 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # pa = [root]
        # chd = []
        # while not all(node is None for node in pa):
        #     for p in pa:
        #         if p: chd = chd + [p.left] + [p.right]
        #     vallist = []
        #     for c in chd:
        #         if c: vallist.append(c.val)
        #         else: vallist.append(101)
        #     if not vallist == vallist[::-1]: return False
        #     pa, chd = chd, []
        # return True
        def recur(L, R):
                if not L and not R: return True
                if not L or not R or L.val != R.val: return False
                return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)


        
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

