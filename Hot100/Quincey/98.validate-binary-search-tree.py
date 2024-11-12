# @lcpr-before-debug-begin
from python3problem98 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
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
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     def zuoxubianli(root):
    #         if not root:return []
    #         return zuoxubianli(root.left) + [root.val] + zuoxubianli(root.right)
    #     res = zuoxubianli(root)
    #     sres = sorted(res)
    #     for i in range(len(res)-1): 
    #         if sres[i] == sres[i+1] : return False
    #     if res == sorted(res) :return True
    #     else: return False
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and \
               self.isValidBST(root.left, left, x) and \
               self.isValidBST(root.right, x, right)

        
        
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

