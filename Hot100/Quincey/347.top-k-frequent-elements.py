# @lcpr-before-debug-begin
from python3problem347 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        count = collections.Counter(nums)
        return [item[0] for item in count.most_common(k)]

# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

