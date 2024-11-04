#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i,j = 0, 0
        m, n = len(matrix), len(matrix[0])
        N = m*n
        I = [0]
        J = [0]
        res = []
        while  len(res) < N:
            res.append(matrix[i][j])
            matrix[i][j] = 101
            if i == 0 and j == 0: 
                if n == 1:
                    i += 1
                else:
                    j += 1
            elif J[-1] - J[-2] == 1: # 上一步向右走
                if J[-1] < n-1 and matrix[I[-1]][J[-1] + 1] <= 100: # 没到拐角
                    j += 1
                else:
                    i += 1
            elif J[-1] - J[-2] == -1: # 上一步向左走
                if J[-1] > 0 and matrix[I[-1]][J[-1] - 1] <= 100:
                    j -= 1
                else:
                    i -= 1
            elif I[-1] - I[-2] == 1: # 上一步向下走
                if I[-1] < m -1 and matrix[I[-1] + 1][J[-1]] <= 100:
                    i += 1
                else:
                    j -= 1
            elif I[-1] - I[-2] == -1: # 上一步向上走
                if I[-1] > 0 and matrix[I[-1] - 1][J[-1]] <= 100:
                    i -= 1
                else:
                    j += 1
            I.append(i)
            J.append(j)
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

