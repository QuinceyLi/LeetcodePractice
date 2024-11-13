#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第 K 小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 二叉搜索树的中序遍历为递增序列。
        # def xianxu(root):
        #     if not root: return []
        #     return xianxu(root.left) + [root.val] + xianxu(root.right)
        # res = xianxu(root)
        # return res[k-1]
        def dfs(root):
            if not root:return
            dfs(root.left)
            if self.k == 0:return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.right)
        self.k = k
        dfs(root)
        return self.res

        
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

