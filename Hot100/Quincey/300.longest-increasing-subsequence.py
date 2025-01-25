#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # @cache
        # def dfs(i, ss):
        #     if i == n:
        #         return 0
        #     if nums[i] <= ss:
        #         return dfs(i+1, ss)
        #     return max(dfs(i+1, ss), dfs(i+1, max(ss,nums[i]))+1)
        # return dfs(0, -inf)
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1  # 加一提到循环外面
        return max(dfs(i) for i in range(len(nums)))
# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

