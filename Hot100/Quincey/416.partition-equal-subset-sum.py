#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i < 0:
                return True if j==0 else False
            if nums[i] <= j:
                return dfs(i-1, j) or dfs(i-1, j-nums[i])
            else: return dfs(i-1, j)
        s = sum(nums)
        return s%2 == 0 and dfs(len(nums)-1, s // 2)
              
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

