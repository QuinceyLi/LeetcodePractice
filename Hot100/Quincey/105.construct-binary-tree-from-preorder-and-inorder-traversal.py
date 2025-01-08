#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # root = TreeNode(preorder[0])
        # n = len(preorder)
        # if n == 1: return root
        # hmap1,hmap2 = {},{}
        # for v1 in preorder:
        #     hmap2[v1] = None
        #     for i in range(n):
        #         if v1 == inorder[i]: hmap1[v1] = i
        # hmap2[preorder[0]] = root
        # for i in range(1,n):
        #     if hmap1[preorder[i]] < hmap1[preorder[i-1]]: # 先序遍历的下一个点在中序遍历的左侧
        #         hmap2[preorder[i-1]].left = TreeNode(preorder[i])
        #     else:
        def recur(root, left, right):
            if left > right: return                               # 递归终止
            node = TreeNode(preorder[root])                       # 建立根节点
            i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
            node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
            return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)

# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

