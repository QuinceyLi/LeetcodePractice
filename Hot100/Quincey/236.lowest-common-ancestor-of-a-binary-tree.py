# @lcpr-before-debug-begin
from python3problem236 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tobefind,result = [p.val, q.val],[]
        def dfs(root):
            if not root or not tobefind: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val in tobefind: 
                mid = 1
                tobefind.remove(root.val)
            else: mid = 0
            if left + right + mid == 2: result.append(root)
            return left + right + mid           
        dfs(root)
        return result[0]


# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

