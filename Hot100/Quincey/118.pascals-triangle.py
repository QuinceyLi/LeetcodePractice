# @lcpr-before-debug-begin
from python3problem118 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]
        else:
            ans.append([1])
            ans.append([1,1])
            for i in range(3, numRows+1):
                temp = [1] * i
                for j in range(1, i-1):
                    temp[j] = ans[-1][j-1] + ans[-1][j]
                ans.append(temp.copy())
        return ans
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

