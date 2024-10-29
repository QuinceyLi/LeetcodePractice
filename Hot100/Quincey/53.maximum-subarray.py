# @lcpr-before-debug-begin
from python3problem53 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = nums[0]
        dp = [M]
        if len(nums) == 1:
            return M
        for i in range(1,len(nums)):
            dp.append(max(nums[i], dp[-1]+nums[i]))
        return max(dp)
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

