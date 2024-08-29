# @lcpr-before-debug-begin
from python3problem560 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hx = {0:1}
        res = 0
        pre_num = 0
        for num in nums:
            pre_num = pre_num + num
            if pre_num - k in hx:
                res += hx[pre_num - k]
            if pre_num in hx:
                hx[pre_num] += 1
            else:
                hx[pre_num] = 1
        return res

# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

