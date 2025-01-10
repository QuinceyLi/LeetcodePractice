# @lcpr-before-debug-begin
from python3problem78 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        ans = []
        path = []
        def dfs(i):
            if i == L:
                ans.append(path.copy())
                return
            dfs(i+1)

            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans


# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

