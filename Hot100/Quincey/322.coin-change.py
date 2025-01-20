#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        @cache
        def dfs(k, c):
            if k < 0:
                return 0 if c ==0 else inf
            if coins[k] > c:
                return dfs(k-1, c)
            return min(dfs(k-1, c), dfs(k, c-coins[k])+1)
        ans = dfs(n-1, amount)
        return ans if ans<inf else -1
        
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

