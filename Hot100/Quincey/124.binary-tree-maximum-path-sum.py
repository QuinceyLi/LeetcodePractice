#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1001
        def dfs(node):
            if not node: return 0
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_sum + r_sum + node.val, l_sum + node.val, r_sum + node.val, node.val)
            return max(l_sum, r_sum, 0) + node.val
        dfs(root)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

