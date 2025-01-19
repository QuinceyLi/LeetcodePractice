#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30204
#
# [198] 打家劫舍
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Maxmoney = 0
        # n = len(nums)
        # @cache
        # def tou(ketou, money):
        #     if ketou >= n:
        #         nonlocal Maxmoney
        #         Maxmoney = max(money, Maxmoney)
        #         return
        #     for kt in range(ketou, n):
        #         tou(kt+2, money+nums[kt])
        # tou(0, 0)
        # return Maxmoney
        n = len(nums)
        @cache
        def dfs(i):
            if i < 0: return 0
            return max(dfs(i-1), dfs(i-2) + nums[i])
        return dfs(n-1)

# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

