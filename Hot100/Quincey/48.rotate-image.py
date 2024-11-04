# @lcpr-before-debug-begin
from python3problem48 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # import numpy as np
        # n = len(matrix)
        # matrix = np.array(matrix)
        # nrotate = int(n/2)
        # i=0
        # while i < nrotate:
        #     # L = round(n/(i+1)) # 旋转的子矩阵的长度
        #     l,r,t,b = i, n-1-i, i, n-1-i
        #     temp = matrix[t][l]
        #     matrix[t][l] = matrix[b][l]
        #     matrix[b][l] = matrix[b][r]
        #     matrix[b][r] = matrix[t][r]
        #     matrix[t][r] = temp
        #     if r - l > 1:
        #         temp = matrix[t][l+1:r].copy()
        #         matrix[t][l+1:r] = np.flip(matrix[t+1:b,l])
        #         matrix[t+1:b,l] = matrix[b][l+1:r]
        #         matrix[b][l+1:r] = np.flip(matrix[t+1:b,r])
        #         matrix[t+1:b,r] = temp
        #     i += 1
        # return matrix
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp



        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

