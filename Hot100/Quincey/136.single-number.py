#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30204
#
# [136] 只出现一次的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for k in set(nums):
        #     nums.remove(k)
        #     if k in nums:pass
        #     else: return k
            
        return reduce(xor, nums)
# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

