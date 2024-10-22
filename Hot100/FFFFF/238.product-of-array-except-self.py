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
        n = len(nums)
        l = [0]*n
        l[0] = 1
        for i in range(1,n):
            l[i] = nums[i-1]*l[i-1]
        
        r=1
        for j in range(n)[::-1]:
            l[j] = l[j]*r
            r = r*nums[j]
        return l


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

