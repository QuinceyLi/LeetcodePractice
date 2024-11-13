# @lcpr-before-debug-begin
from python3problem114 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
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
    node = None # 前驱节点

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return     # 空节点
        if not self.node:
            self.node = root    # 前驱节点为空，首个节点直接记录
        else:
            # 否则将当前节点拼接到前驱节点之后，并更新前驱节点
            self.node.left = None
            self.node.right = root
            self.node = self.node.right
        r = root.right    # 暂存节点的右子树，避免递归过程中右子树信息丢失
        self.flatten(root.left) # 递归左子树
        self.flatten(r) # 递归右子树
                
            




            
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

