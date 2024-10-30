#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, temp = [1]*len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            ans[i] *= temp
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

