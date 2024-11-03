#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(m+n)
        # row = len(matrix)
        # col = len(matrix[0])
        # rowset = set()
        # colset = set()

        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == 0:
        #             rowset.add(i)
        #             colset.add(j)

        # for i in range(row):
        #     for j in range(col):
        #         if i in rowset or j in colset:
        #             matrix[i][j] = 0
        
        # return matrix

        # O(1)
        rowflag = False
        colflag = False

        row = len(matrix)
        col = len(matrix[0])

        for j in range(col):
            if matrix[0][j] == 0:
                colflag = True
                break
        for i in range(row):
            if matrix[i][0] == 0:
                rowflag = True
                break
        
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == 0:
                    matrix[0][j],matrix[i][0] = 0,0
        
        for i in range(1,row):
            for j in range(1,col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if rowflag:
            for i in range(row):
                matrix[i][0] = 0
        if colflag:
            for j in range(col):
                matrix[0][j] = 0
        return matrix
        
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

